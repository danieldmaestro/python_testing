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

    def customer_deposit(self, currency, amount, wallet_name, customer):
        customer.get_wallet(currency, wallet_name).deposit(amount)

    def setpassword(self, new_password):
        self.password = new_password
        self.default_p = "changed"

    def login(self, username, password):
        if self.is_suspended == "not_suspended":
            if username == self.username and password == self.password:
                self.is_loggedin = True
                print("You have successfully logged in.")
                csvlogger.staff([self.full_name, "LOGIN", "NIL"])
            else:
                print("Wrong credentials. Try again")
        else:
            print("You are currently suspended. Refer to admin.")
            

    def logout(self):
        if self.is_loggedin:
            self.is_loggedin = False
            print("You have successfully logged out.")
            csvlogger.staff([self.full_name, "LOGOUT", "NIL"])
        else:
            print("You have to be logged in to log out.")

    def __str__(self):
        return self.full_name
