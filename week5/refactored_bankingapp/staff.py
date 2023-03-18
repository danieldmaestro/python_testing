class Staff:
    def __init__(self, f_name:str, l_name:str, username:str, password:str, suspension_status="not_suspended", default_p = "not_changed"):
        self.f_name = f_name
        self.l_name = l_name
        self.password = password
        self.username = username
        self.full_name = self.f_name + " " + self.l_name
        self.is_suspended = suspension_status
        self.is_loggedin = False
        self.default_p = default_p

    def customer_deposit(self, currency, amount, wallet_name, customer_email):
        customer.get_wallet(currency, wallet_name).deposit(amount)
