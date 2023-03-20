from random import randint
from wallet import Wallet
from csv_logger import CsvLogger
import logging

filename = "logs.csv"
delimiter = ','
level = logging.INFO
custom_additional_levels = ['customer']
fmt = f'%(asctime)s{delimiter}%(levelname)s{delimiter}%(message)s'
datefmt = '%Y/%m/%d %H:%M:%S'
max_size = 10240  # 1 megabyte
max_files = 4  # 4 rotating files
header = ['date/time', 'user-class', 'user-name', 'action', 'amount']

csvlogger = CsvLogger(filename=filename,
                      delimiter=delimiter,
                      level=level,
                      add_level_names=custom_additional_levels,
                      add_level_nums=None,
                      fmt=fmt,
                      datefmt=datefmt,
                      max_size=max_size,
                      max_files=max_files,
                      header=header)

class Customer:
    def __init__(self, f_name:str, l_name:str, phone_no:str, acct_type:str, pin, email:str):
        self.f_name = f_name
        self.l_name = l_name
        self.phone_no = phone_no
        self.acct_type = acct_type
        self.pin = pin
        self.email = email
        self.is_loggedin = False
        self.full_name = self.f_name + " " + self.l_name
        self._wallets = {
            'NGN': {},
            'USD': {},
            'GBP': {}
        }
    
    @property
    def wallets(self):
        return self._wallets

    def wallet_names(self):
        for wal in self._wallets.values():
            if wal:
                for w in wal.keys():
                    print(w)
    
    def add_wallet(self, currency, new_wallet, wallet_name):
        self._wallets[currency][wallet_name] = new_wallet

    def create_wallet(self, currency, wallet_name):
        n_wallet = Wallet(self.email, currency, wallet_name)
        self.add_wallet(currency, n_wallet, wallet_name)
        print(f"You have successfully created your new {currency} wallet.")

    def get_wallet(self, currency, wallet_name):
        return self._wallets[currency][wallet_name]

    def show_all_wallets(self):
        gross_wallet_balance = 0
        gross_inflow = 0
        gross_outflow = 0
        # print(self._wallets.items())

        for wal_curr, wal in self._wallets.items():
            if wal:
                if wal_curr == 'USD':
                    for usd_wal in wal.values():
                        gross_wallet_balance += usd_wal.current_balance * 735
                        gross_inflow += usd_wal.total_inflow * 735
                        gross_outflow += usd_wal.total_outflow * 735
                
                elif wal_curr == 'GBP':
                    for gbp_wal in wal.values():
                        gross_wallet_balance += gbp_wal.current_balance * 910
                        gross_inflow += gbp_wal.total_inflow * 910
                        gross_outflow += gbp_wal.total_outflow * 910

                elif wal_curr == "NGN":
                    for ngn_wal in wal.values():
                        gross_wallet_balance += ngn_wal.current_balance
                        gross_inflow += ngn_wal.total_inflow
                        gross_outflow += ngn_wal.total_outflow
                    
        print('==========================================')
        print(f"Dear {self.full_name}, here's your wallet overview:")
        for curr_wallet in self._wallets.values():
            for wal in curr_wallet.values():
                if wal:
                    print('==========================================')
                    wal.display_wallet()
        print('==========================================')
        print(f"TOTAL RECEIVED: ₦{gross_inflow:,.2f}")
        print(f"TOTAL SENT: ₦{gross_outflow:,.2f}")
        print(F"TOTAL USER BALANCE: ₦{gross_wallet_balance:,.2f}")

    def login(self, email, pin):
        if email == self.email and pin == self.pin:
            self.is_loggedin = True
            print("You have successfully logged in.")
            csvlogger.customer([self.full_name, "LOGIN", "NIL"])
        else:
            print("Wrong Credentials. Try again.")

    def logout(self):
        if self.is_loggedin:
            self.is_loggedin = False
            print("You have successfully logged out.")
            csvlogger.customer([self.full_name, "LOGOUT", "NIL"])
        else:
            print("You have to be logged in to log out.")
    
    def __str__(self):
        return self.full_name

# acct_no=str(randint(1324145265, 5628158894))
danny = Customer('Daniel', 'Momodu', '09032115544', "Savings", 1234, "danny@gmail.com")
danny.create_wallet('NGN', "Fees Wallet")
danny.create_wallet('NGN', "Nepa Wallet")
danny.create_wallet('USD', "Netflix Wallet")
danny.create_wallet('USD', "Starlink Wallet")

danny_fees = danny.get_wallet('NGN', "Fees Wallet")
danny_nepa = danny.get_wallet('NGN', "Nepa Wallet")
danny_netflix = danny.get_wallet('USD', "Netflix Wallet")
danny_starlink = danny.get_wallet('USD', "Starlink Wallet")

danny_fees.deposit(5000)
danny_netflix.deposit(200)
danny_fees.withdrawal(900)
danny_netflix.withdrawal(23)
danny_nepa.deposit(3000)
danny_starlink.deposit(500)
danny.show_all_wallets()
# print(danny.wallet)
# print(danny.wallet('USD'))





