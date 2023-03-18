from random import randint
from wallet import Wallet

class Customer:
    def __init__(self, f_name, l_name, phone_no, acct_type, pin, email, acct_no=str(randint(1324145265, 5628158894))):
        self.f_name = f_name
        self.l_name = l_name
        self.phone_no = phone_no
        self.acct_type = acct_type
        self.pin = pin
        self.email = email
        self.is_loggedin = False
        self.acct_no = acct_no
        self.full_name = self.f_name + " " + self.l_name
        self._wallets = {
            'NGN': None,
            'USD': None,
            'GBP': None
        }

    @property
    def wallet(self, currency):
        return self._wallets[currency] 
    
    @wallet.setter
    def wallet(self, currency, new_wallet):
        self._wallets[currency] = new_wallet

    def create_wallet(self, currency):
        n_wallet = Wallet(currency)
        self.wallet(currency, n_wallet)


