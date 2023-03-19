from csv_logger import CsvLogger
import logging

filename = "logs.csv"
delimiter = ','
level = logging.INFO
custom_additional_levels = ['customer', 'wallet', 'staff', 'admin']
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

class Wallet:
    def __init__(self, user_email:str, currency:str, wallet_name:str):
        self._current_balance = 0
        self._previous_balance = 0
        self._user_email = user_email
        self._currency = currency
        self._wallet_name = wallet_name
        self._outflow = 0
        self._inflow = 0

    @property
    def user_email(self):
        return self._user_email            

    @property
    def current_balance(self):
        return self._current_balance
    
    @current_balance.setter
    def current_balance(self, value):
        if value > 0:
            self._current_balance = value
        else:
            raise ValueError("Value must be above 0")
        
    @property
    def previous_balance(self):
        return self._previous_balance
    
    @previous_balance.setter
    def previous_balance(self, value):
        self._previous_balance = value
        
    @property
    def currency(self):
        return self._currency
    
    @property
    def wallet_name(self):
        return self._wallet_name
    
    @property
    def c_sign(self):
        if self.currency == "NGN":
            return '₦'
        elif self.currency == 'USD':
            return '$'
        elif self.currency == 'GBP':
            return '£'
    
    @property
    def total_outflow(self):
        return self._outflow
    
    @total_outflow.setter
    def total_outflow(self, value):
        self._outflow = value

    @property
    def total_inflow(self):
        return self._inflow
    
    @total_inflow.setter
    def total_inflow(self, value):
        self._inflow = value

    def view_current_balance(self):
        # view = locale.currency(self.current_balance, grouping=True)
        print(f"Your {self.currency} balance is {self.c_sign}{self.current_balance:,.2f}")
    
    def deposit(self, amount):
        self.previous_balance = self.current_balance
        self.current_balance += amount
        self.total_inflow += amount
        # view_amt = locale.currency(amount, grouping=True)
        # view_bal = locale.currency(self.current_balance, grouping=True)
        print('==========================================')
        print(f"{self.c_sign}{amount:,.2f} has been deposited into your account")
        print(f"Your current balance is {self.c_sign}{self.current_balance:,.2f}")

    def inflow(self, amount):
        self.previous_balance = self.current_balance
        self.current_balance += amount
        self.total_inflow += amount

    def withdrawal(self, amount):
        if self.current_balance >= amount:
            self.previous_balance = self.current_balance
            self.current_balance -= amount
            self.total_outflow = amount
            # view_amt = locale.currency(amount, grouping=True)
            # view_bal = locale.currency(self.current_balance, grouping=True)
            print('==========================================')
            print(f"You have successfully withdrawn {self.c_sign}{amount:,.2f}")
            print(f"Your current balance is {self.c_sign}{self.current_balance:,.2f}")
        else:
            print("Withdrawal amount greater than wallet balance.")
    
    def transfer(self, amount, recipient, wallet_name):
        if self.current_balance >= amount:
            self.previous_balance = self.current_balance
            self.current_balance -= amount
            self.total_outflow -= amount
            recipient.get_wallet(self.currency, wallet_name).inflow(amount) 
            # view_amt = locale.currency(amount, grouping=True)
            # view_bal = locale.currency(self.current_balance, grouping=True)
            print('==========================================')
            print(f"You have successfully transferred {self.c_sign}{amount:,.2f}")
            print(f"Your current balance is {self.c_sign}{self.current_balance:,.2f}")
        else:
            print("Transfer amount must be less than wallet balance")

    def display_wallet(self):
        print('==========================================')
        print(f"{self.wallet_name}({self.currency}):\nCURRENT WALLET BALANCE: {self.c_sign}{self.current_balance:,.2f}     PREVIOUS WALLET BALANCE: {self.c_sign}{self.previous_balance:,.2f}\nTOTAL RECEIVED: {self.c_sign}{self.total_inflow:,.2f}\nTOTAL SENT: {self.c_sign}{self.total_outflow:,.2f}\n")

    def __str__(self):
        return (f"{self.wallet_name} ({self.currency}): Balance -> {self.c_sign}{self.current_balance:,.2f}")



# wallet1 = Wallet('NGN')

# wallet1.deposit(5000)
# wallet1.withdrawal(400)
# print(wallet1._inflow)
# print(wallet1._outflow)

