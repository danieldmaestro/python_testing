import locale

locale.setlocale(locale.LC_ALL, "en-NG")

class Wallet:
    def __init__(self, currency):
        self._balance = 0
        self._currency = currency
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
        view = locale.currency(self.current_balance, grouping=True)
        print(f"Your {self._currency} balance is {view}")
    
    def deposit(self, amount):
        self.current_balance += amount
        self.total_inflow += amount
        view_amt = locale.currency(amount, grouping=True)
        view_bal = locale.currency(self.current_balance, grouping=True)
        print(f"{view_amt} has been deposited into your account")
        print('==========================================')
        print(f"Your current balance is {view_bal}")

    def inflow(self, amount):
        self.current_balance += amount
        self.total_inflow += amount

    def withdrawal(self, amount):
        if self.current_balance >= amount:
            self.current_balance -= amount
            self.total_outflow = amount
            view_amt = locale.currency(amount, grouping=True)
            view_bal = locale.currency(self.current_balance, grouping=True)
            print(f"You have successfully withdrawn {view_amt}")
            print('==========================================')
            print(f"Your current balance is {view_bal}")
        else:
            print("Withdrawal amount greater than wallet balance.")
    
    def transfer(self, amount, recipient):
        if self.current_balance >= amount:
            self.current_balance -= amount
            self.total_outflow -= amount
            recipient.wallet(self._currency).inflow(amount) 
            view_amt = locale.currency(amount, grouping=True)
            view_bal = locale.currency(self.current_balance, grouping=True)
            print(f"You have successfully transferred {view_amt}")
            print('==========================================')
            print(f"Your current balance is {view_bal}")
        else:
            pass




wallet1 = Wallet('NGN')

wallet1.deposit(5000)
wallet1.withdrawal(400)
print(wallet1._inflow)
print(wallet1._outflow)

