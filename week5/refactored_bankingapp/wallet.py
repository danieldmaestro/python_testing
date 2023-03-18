import locale

# locale.setlocale(locale.LC_ALL, "en-NG")

class Wallet:
    def __init__(self, currency:str, wallet_name:str):
        self._balance = 0
        self._currency = currency
        self._wallet_name = wallet_name
        self._outflow = 0
        self._inflow = 0            

    @property
    def current_balance(self):
        return self._balance
    
    @current_balance.setter
    def current_balance(self, value):
        if value > 0:
            self._balance = value
        else:
            raise ValueError("Value must be above 0")
        
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
        self.current_balance += amount
        self.total_inflow += amount
        # view_amt = locale.currency(amount, grouping=True)
        # view_bal = locale.currency(self.current_balance, grouping=True)
        print('==========================================')
        print(f"{self.c_sign}{amount:,.2f} has been deposited into your account")
        print(f"Your current balance is {self.c_sign}{self.current_balance:,.2f}")

    def inflow(self, amount):
        self.current_balance += amount
        self.total_inflow += amount

    def withdrawal(self, amount):
        if self.current_balance >= amount:
            self.current_balance -= amount
            self.total_outflow = amount
            # view_amt = locale.currency(amount, grouping=True)
            # view_bal = locale.currency(self.current_balance, grouping=True)
            print('==========================================')
            print(f"You have successfully withdrawn {self.c_sign}{amount:,.2f}")
            print(f"Your current balance is {self.c_sign}{self.current_balance:,.2f}")
        else:
            print("Withdrawal amount greater than wallet balance.")
    
    def transfer(self, amount, recipient):
        if self.current_balance >= amount:
            self.current_balance -= amount
            self.total_outflow -= amount
            recipient.get_wallet(self.currency).inflow(amount) 
            # view_amt = locale.currency(amount, grouping=True)
            # view_bal = locale.currency(self.current_balance, grouping=True)
            print('==========================================')
            print(f"You have successfully transferred {self.c_sign}{amount:,.2f}")
            print(f"Your current balance is {self.c_sign}{self.current_balance:,.2f}")
        else:
            print("Transfer amount must be less than wallet balance")

    def display_wallet(self):
        print('==========================================')
        print(f"{self.wallet_name}({self.currency}):\nWALLET BALANCE: {self.c_sign}{self.current_balance:,.2f}\nTOTAL RECEIVED: {self.c_sign}{self.total_inflow:,.2f}\nTOTAL SENT: {self.c_sign}{self.total_outflow:,.2f}\n")

    def __str__(self):
        return (f"{self.wallet_name} ({self.currency}): Balance -> {self.c_sign}{self.current_balance:,.2f}")



# wallet1 = Wallet('NGN')

# wallet1.deposit(5000)
# wallet1.withdrawal(400)
# print(wallet1._inflow)
# print(wallet1._outflow)

