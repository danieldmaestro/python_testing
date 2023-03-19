from random import choice
import string
from csv_logger import CsvLogger
import logging
from staff import Staff

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

class Admin:
    def __init__(self, f_name, l_name, username, password):
        self.f_name = f_name
        self.l_name = l_name
        self.full_name = self.f_name + " " + self.l_name
        self.username = username
        self.password = password
        self.is_loggedin = False

    def create_staff(self, f_name, l_name, username, password =''.join((choice(string.ascii_letters) for i in range(8)))):
        print(f"New Staff Created. Your default password is {password}")
        return Staff(f_name, l_name, username, password)

    def suspension(self, staff):
        staff.is_suspended = "suspended"
        print(f"{staff.f_name} is hereby suspended.")

    def end_suspension(self, staff):
        staff.is_suspended = "not_suspended"
        print(f"Dear {staff.f_name}, your suspension status has been lifted.")

    def login(self, username, password):
        if username == self.username and password == self.password:
            self.is_loggedin = True
            print("You have successfully logged in.")
            csvlogger.admin([self.full_name, "LOGIN", "NIL"])
        else:
            print("Wrong credentials. Try again")

    def logout(self):
        if self.is_loggedin:
            self.is_loggedin = False
            print("You have successfully logged out.")
            csvlogger.admin([self.full_name, "LOGOUT", "NIL"])
        else:
            print("You have to be logged in to log out.")
