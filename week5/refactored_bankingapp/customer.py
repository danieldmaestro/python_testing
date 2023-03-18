from random import randint
from wallet import Wallet

class Customer:
    def __init__(self, f_name, l_name, phone_no, acct_type, pin, email):
        self.f_name = f_name
        self.l_name = l_name
        self.phone_no = phone_no
        self.acct_type = acct_type
        self.pin = pin
        self.email = email
        self.is_loggedin = False
        self.full_name = self.f_name + " " + self.l_name
        self._wallets = {
            'NGN': None,
            'USD': None,
            'GBP': None
        }

    @property
    def wallet(self):
        for w in self._wallets.values():
            if w:
                print(w)
    
    def add_wallet(self, currency, new_wallet):
        self._wallets[currency] = new_wallet

    def create_wallet(self, currency):
        n_wallet = Wallet(currency)
        self.add_wallet(currency, n_wallet)
        print(f"You have successfully created your {currency} wallet.")

    def get_wallet(self, currency):
        return self._wallets[currency]

    def show_all_wallets(self):
        gross_wallet_balance = 0
        gross_inflow = 0
        gross_outflow = 0
        # print(self._wallets.items())

        for curr, wal in self._wallets.items():
            if wal:
                if curr == 'USD':
                    gross_wallet_balance += wal.current_balance * 735
                    gross_inflow += wal.total_inflow * 735
                    gross_outflow += wal.total_outflow * 735
                elif curr == 'GBP':
                    gross_wallet_balance += wal.current_balance * 910
                    gross_inflow += wal.total_inflow * 910
                    gross_outflow += wal.total_outflow * 910
                else:
                    gross_wallet_balance += wal.current_balance
                    gross_inflow += wal.total_inflow
                    gross_outflow += wal.total_outflow

        print(f"Dear {self.full_name}, here's your wallet overview:\n")
        print('=========================================================')
        for wal in self._wallets.values():
            if wal:
                wal.display_wallet()
                print("=========================================================")
        print(f"TOTAL RECEIVED: ₦{gross_inflow}")
        print(f"TOTAL SENT: ₦{gross_outflow}")
        print(F"TOTAL USER BALANCE: ₦{gross_wallet_balance}")


# acct_no=str(randint(1324145265, 5628158894))
danny = Customer('Daniel', 'Momodu', '09032115544', "Savings", 1234, "danny@gmail.com")
danny.create_wallet('NGN')
danny.create_wallet('USD')
dannyNGN = danny.get_wallet('NGN')
dannyUSD = danny.get_wallet('USD')
dannyNGN.deposit(5000)
dannyUSD.deposit(200)
dannyNGN.withdrawal(900)
dannyUSD.withdrawal(23)
danny.show_all_wallets()
# print(danny.wallet)
# print(danny.wallet('USD'))





