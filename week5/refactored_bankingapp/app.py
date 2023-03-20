# from customer import Customer
# from staff import Staff
# from wallet import Wallet
# from admin import Admin
from customer_database import CustomerDatabase
from staff_database import StaffDatabase
from random import choice
import string
import re
from csv import reader
import pickle
from csv_logger import CsvLogger
import time
import logging


filename = "logs.csv"
delimiter = ','
level = logging.INFO
custom_additional_levels = ['customer', 'staff', 'admin']
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

    def wallet_names(self, currency):
        print("Getting Wallets....")
        time.sleep(2)
        print(f"AVAILABLE {currency} WALLETS: ")
        for wal in self._wallets[currency].keys():
            if wal:
                print("->", wal)
    
    def add_wallet(self, currency, new_wallet, wallet_name):
        self._wallets[currency][wallet_name] = new_wallet

    def create_wallet(self, currency, wallet_name):
        print(f"Creating {currency} Wallet...")
        time.sleep(2)
        n_wallet = Wallet(self.full_name, currency, wallet_name)
        self.add_wallet(currency, n_wallet, wallet_name)
        print(f"You have successfully created your new {currency} wallet.")

    def get_wallet(self, currency, wallet_name):
        print("Getting Wallet...")
        time.sleep(1.5)
        return self._wallets[currency][wallet_name]

    def show_all_wallets(self):
        print("Collating all wallet balances....")
        time.sleep(3)
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
        print("Logging in....")
        time.sleep(1.5)
        if email == self.email and pin == self.pin:
            self.is_loggedin = True
            print("You have successfully logged in.")
            csvlogger.customer([self.full_name, "LOGIN", "NIL"])
        else:
            print("Wrong Credentials. Try again.")

    def logout(self):
        print("Logging out....")
        time.sleep(1.5)
        if self.is_loggedin:
            self.is_loggedin = False
            print("You have successfully logged out.")
            csvlogger.customer([self.full_name, "LOGOUT", "NIL"])
        else:
            print("You have to be logged in to log out.")
    
    def __str__(self):
        return self.full_name

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
        # csvlogger.customer([customer.full_name, "DEPOSIT", amount])

    def setpassword(self, new_password):
        print("Loading...")
        time.sleep(1)
        self.password = new_password
        self.default_p = "changed"
        print("Password reset successful")

    def login(self, username, password):
        print("Logging in....")
        time.sleep(1)
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
        print("Logging out....")
        time.sleep(1)
        if self.is_loggedin:
            self.is_loggedin = False
            print("You have successfully logged out.")
            csvlogger.staff([self.full_name, "LOGOUT", "NIL"])
        else:
            print("You have to be logged in to log out.")

    def __str__(self):
        return self.full_name
    
class Admin:
    def __init__(self, f_name, l_name, username, password):
        self.f_name = f_name
        self.l_name = l_name
        self.full_name = self.f_name + " " + self.l_name
        self.username = username
        self.password = password
        self.is_loggedin = False

    def create_staff(self, f_name, l_name, username, password =''.join((choice(string.ascii_letters) for i in range(8)))):
        print("Creating new staff....")
        time.sleep(2)
        print(f"New Staff Created. Your default password is {password}")
        return Staff(f_name, l_name, username, password)

    def suspension(self, staff):
        print("Loading...")
        time.sleep(1)
        staff.is_suspended = "suspended"
        print(f"{staff.f_name} is hereby suspended.")

    def end_suspension(self, staff):
        print("Loading...")
        time.sleep(1)
        staff.is_suspended = "not_suspended"
        print(f"Dear {staff.f_name}, your suspension status has been lifted.")

    def login(self, username, password):
        print("Logging in...")
        time.sleep(1)
        if username == self.username and password == self.password:
            self.is_loggedin = True
            print("You have successfully logged in.")
            csvlogger.admin([self.full_name, "LOGIN", "NIL"])
        else:
            print("Wrong credentials. Try again")

    def logout(self):
        print("Logging out...")
        time.sleep(1)
        if self.is_loggedin:
            self.is_loggedin = False
            print("You have successfully logged out.")
            csvlogger.admin([self.full_name, "LOGOUT", "NIL"])
        else:
            print("You have to be logged in to log out.")


class Wallet:
    def __init__(self, user_fname:str, currency:str, wallet_name:str):
        self._current_balance = 0
        self._previous_balance = 0
        self._user_fname = user_fname
        self._currency = currency
        self._wallet_name = wallet_name
        self._outflow = 0
        self._inflow = 0
            
    @property
    def user_fname(self):
        return self._user_fname
    
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
        print('Loading...')
        time.sleep(1)
        self.previous_balance = self.current_balance
        self.current_balance += amount
        self.total_inflow += amount
        # view_amt = locale.currency(amount, grouping=True)
        # view_bal = locale.currency(self.current_balance, grouping=True)
        print('==========================================')
        print(f"{self.c_sign}{amount:,.2f} has been deposited into your wallet.")
        print(f"Your current balance is {self.c_sign}{self.current_balance:,.2f}")
        csvlogger.customer([self.user_fname, "DEPOSIT", amount])

    def inflow(self, amount):
        time.sleep(1)
        self.previous_balance = self.current_balance
        self.current_balance += amount
        self.total_inflow += amount
        csvlogger.customer([self.user_fname, "INFLOW", amount])


    def withdrawal(self, amount):
        print("Loading....")
        time.sleep(1)
        if self.current_balance >= amount:
            self.previous_balance = self.current_balance
            self.current_balance -= amount
            self.total_outflow += amount
            # view_amt = locale.currency(amount, grouping=True)
            # view_bal = locale.currency(self.current_balance, grouping=True)
            print('==========================================')
            print(f"You have successfully withdrawn {self.c_sign}{amount:,.2f}")
            print(f"Your current balance is {self.c_sign}{self.current_balance:,.2f}")
            csvlogger.customer([self.user_fname, "WITHDRAWAL", amount])

        else:
            print("Withdrawal amount greater than wallet balance.")
    
    def transfer(self, amount, recipient, wallet_name):
        print("Loading...")
        time.sleep(1)
        if self.current_balance >= amount:
            self.previous_balance = self.current_balance
            self.current_balance -= amount
            self.total_outflow += amount
            recipient.get_wallet(self.currency, wallet_name).inflow(amount) 
            # view_amt = locale.currency(amount, grouping=True)
            # view_bal = locale.currency(self.current_balance, grouping=True)
            print('==========================================')
            print(f"You have successfully transferred {self.c_sign}{amount:,.2f}")
            print(f"Your current balance is {self.c_sign}{self.current_balance:,.2f}")
            csvlogger.customer([self.user_fname, "TRANSFER", amount])

        else:
            print("Transfer amount must be less than wallet balance")

    def display_wallet(self):
        print('==========================================')
        print(f"{self.wallet_name}({self.currency}):\nCURRENT WALLET BALANCE: {self.c_sign}{self.current_balance:,.2f}     PREVIOUS WALLET BALANCE: {self.c_sign}{self.previous_balance:,.2f}\nTOTAL RECEIVED: {self.c_sign}{self.total_inflow:,.2f}\nTOTAL SENT: {self.c_sign}{self.total_outflow:,.2f}\n")

    def __str__(self):
        return (f"{self.wallet_name} ({self.currency}): Balance -> {self.c_sign}{self.current_balance:,.2f}")
    

class GetOutOfLoop( Exception ):
    pass
try:
    with open('customer_db.pickle', 'rb') as file:
        customer_db = pickle.load(file)
except EOFError:
    customer_db = CustomerDatabase()

try:
    with open('staff_db.pickle', 'rb') as file:
        staff_db = pickle.load(file)
except EOFError:
    staff_db = StaffDatabase()

admin = Admin("Daniel", "Momodu", "Dmaestro", "sapa&cruise")
app_state = True
while app_state:
    log_or_sign = input(
        "MAIN MENU\nWhat do you want to do?\n\n1.LOGIN SCREEN\n2. SIGN UP SCREEN\n0. CLOSE APP\n\nINPUT: ")
    login = True
    time.sleep(0.5)
    while login:
        if log_or_sign == "1":
            # while loop makes sure you're inputting valid queries
            while True:
                # input for choice of login. while loop to make sure correct input is put in
                u_type = input(
                    "LOGIN SCREEN\nChoose type of user\n\n1. ADMIN\n2. STAFF\n3. CUSTOMER\n0.MAIN MENU\n\nInput here: ")
                time.sleep(0.5)
                if u_type == "1":
                    #if admin, while loop to make sure of correct username and password 
                    while True:
                        username = input("Type in your username: ")
                        password = input("Type in your password: ")
                        # admin login method to validate username and password
                        admin.login(username, password)
                        if admin.is_loggedin:
                            print("Loading Dashboard...")
                            break
                    
                    time.sleep(2)
                    while admin.is_loggedin:
                        while True:
                            # while loop to choose action for admin
                            print('==========================================')
                            action = input(
                                f"Welcome, {admin.f_name}.\nWhat do you want to do? Here are the inputs\n\n1. Create new Staff\n2. Suspend staff\n3. Remove staff from suspension\n4. View all staff and customer\n5. View all logs\n0.Log out\n\nInput here: ")
                            # CREATE STAFF
                            time.sleep(0.5)
                            if action == "1":
                                print('==========================================')
                                f_name = input("Type in First Name: ")
                                l_name = input("Type in Last Name: ")
                                username = input("Type in Username: ")
                                staff = admin.create_staff(f_name, l_name, username)
                                staff_db.add_staff(staff)
                                break
                            # SUSPEND STAFF 
                            elif action == "2":
                                print('==========================================')
                                s_staff = input("Input Staff username: ")
                                staff = staff_db.get_staff(s_staff)

                                
                                if staff:
                                    # if staff is already suspended, exception message
                                    if staff.is_suspended == "suspended":
                                        print("Staff is already suspended.")
                                        break
                                    else:
                                        admin.suspension(staff)
                                    break
                                else:
                                    print("Staff not found.")
                                    break
                            # REMOVE STAFF FROM SUSPENSION
                            elif action == "3":
                                print('==========================================')
                                s_staff = input("Input Staff username: ")
                                staff = staff_db.get_staff(s_staff)
                                
                                
                                if staff:
                                    if staff.is_suspended == "suspended":
                                        admin.end_suspension(staff)
                                        break
                                    else:
                                        print("Staff is not suspended")
                                    break
                                else:
                                    print("Staff not found.")
                                    break
                            # VIEW ALL STAFF AND CUSTOMERS
                            elif action == "4":
                                # print all staff
                                print("Getting all staff and customers....")
                                time.sleep(2)
                                print('==========================================')
                                print("STAFFS:")
                                print('==========================================')
                                staff_db.all_staff()
                                print('==========================================')
                                print('CUSTOMERS:')
                                print('==========================================')
                                customer_db.all_customers()
                                break
                            # VIEW ALL LOGS
                            elif action == "5":
                                print("Loading....")
                                time.sleep(1)
                                with open("logs.csv") as file:
                                    reader_obj = reader(file)
                                    for row in reader_obj:
                                        if "user-class" not in row:
                                            print(" ".join(row))
                                break
                            elif action == "0":
                                print("Loading....")
                                time.sleep(1)
                                admin.logout()
                                break
                            else:
                                print("Wrong Input. Try again.")
                # STAFF LOGIN
                elif u_type == "2":
                    time.sleep(0.5)
                    try:
                        while True:
                            print('==========================================')
                            username = input("Type in your username: ")
                            password = input("Type in your password: ")

                            staff = staff_db.get_staff(username)

                            print("Loading....")
                            time.sleep(1)
                            if staff:
                                staff.login(username, password)
                                
                                if staff.is_loggedin:
                                # changed default password on first login
                                    if staff.default_p == "not_changed":
                                        print('==========================================')
                                        print(f"Dear, {staff.f_name}, please change your default password.")
                                        new_pword = input("Type in new password: ")
                                        print("Loading....")
                                        time.sleep(1)
                                        staff.setpassword(new_pword)
                                        break
                                    else:
                                        break
                            else:
                                print("Staff not found. Wrong details.")
                                raise GetOutOfLoop
                    except GetOutOfLoop:
                        break
                    print('Loading Dashboard...')
                    time.sleep(1)    
                    while staff.is_loggedin:

                        while True:
                            print('==========================================')
                            action = input(
                                f"Welcome, {staff.f_name}.\nWhat do you want to do? Here are the inputs.\n\n1. View customer balance\n2. Take customer deposit\n0. Logout\n\nInput here: ")
                            time.sleep(0.5)
                            # view customer balance
                            if action == "1":
                                print('==========================================')
                                c_email = input("Customer Email Address: ")
                                customer = customer_db.get_customer(c_email)
                                
                                if customer:
                                    customer.show_all_wallets()
                                    break
                                else:
                                    print("Customer not found.")
                                    break
                            # take customer deposits
                            elif action == "2":
                                print('==========================================')
                                c_email = input("Customer Email Address: ")
                                customer = customer_db.get_customer(c_email)
                                
                                if customer:
                                    while True:
                                        c_curr = input("What currency do you want to deposit?\n1: NGN\n2: USD\n3: GBP\nInput Here: ")
                                        if c_curr == "1":
                                            currency = "NGN"
                                            break
                                        elif c_curr == '2':
                                            currency = "USD"
                                            break
                                        elif c_curr == '3':
                                            currency = "GBP"
                                            break
                                        else:
                                            print("Choose valid input.")
                                    customer.wallet_names(currency)
                                    while True:
                                        print('==========================================')
                                        wallet_name = input("Type in wallet name: ")
                                        if wallet_name in customer.wallets[currency].keys():
                                            break
                                        else:
                                            print('Input correct wallet name from list.')
                                    c_deposit = int(input("Amount to deposit: "))
                            
                                    staff.customer_deposit(currency, c_deposit, wallet_name, customer)
                                    break
                                else:
                                    print("Customer not found.")
                                    break
                            elif action == "0":
                                staff.logout()
                                break
                            else:
                                print("Wrong input. Try again")
                # customer login
                elif u_type == "3":
                    try: 
                        while True:
                            print('==========================================')
                            email = input("Type in your email: ")
                            pin = input("Type in your pin: ")

                            customer = customer_db.get_customer(email)
                            if customer:
                                customer.login(email, pin)
                                if customer.is_loggedin:
                                    break
                            else:
                                raise GetOutOfLoop
                    except GetOutOfLoop:
                        break

                    while customer.is_loggedin:
                        while True:
                            action = input(
                                f"Welcome, {customer.f_name}.\nWhat do you want to do? Here are the inputs:\n\n1. Add New Wallet\n2. View Dashboard\n3. Make a withdrawal\n4. Make a transfer\n5. Delete Account\n0. Logout.\n\nInput Here: ")
                            if action == "1":
                                while True:
                                    c_curr = input("What currency wallet do you want to open?\n1: NGN\n2: USD\n3: GBP\nInput Here: ")
                                    if c_curr == "1":
                                        currency = "NGN"
                                        break
                                    elif c_curr == '2':
                                        currency = "USD"
                                        break
                                    elif c_curr == '3':
                                        currency = "GBP"
                                        break
                                    else:
                                        print("Choose valid input.")
                                
                                wallet_name = input("Name your wallet (e.g School Fees): ") + "Wallet"

                                customer.create_wallet(currency, wallet_name)

                            elif action == "2":
                                customer.show_all_wallets()
                                break
                            elif action == "3":
                                while True:
                                    c_curr = input("What currency do you want to withdraw?\n1: NGN\n2: USD\n3: GBP\nInput Here: ")
                                    if c_curr == "1":
                                        currency = "NGN"
                                        break
                                    elif c_curr == '2':
                                        currency = "USD"
                                        break
                                    elif c_curr == '3':
                                        currency = "GBP"
                                        break
                                    else:
                                        print("Choose valid input.")
                                customer.wallet_names(currency)
                                while True:
                                    wallet_name = input("Type in wallet name: ")
                                    if wallet_name in customer.wallets[currency].keys():
                                        break
                                    else:
                                        print('Input correct wallet name from list.')
                                amount = int(
                                    input("How much do you want to withdraw: "))
                                customer.get_wallet(currency, wallet_name).withdrawal(amount)
                            # make transfer
                            elif action == "4":
                                while True:
                                    c_curr = input("What currency do you want to transfer in?\n1: NGN\n2: USD\n3: GBP\nInput Here: ")
                                    if c_curr == "1":
                                        currency = "NGN"
                                        break
                                    elif c_curr == '2':
                                        currency = "USD"
                                        break
                                    elif c_curr == '3':
                                        currency = "GBP"
                                        break
                                    else:
                                        print("Choose valid input.")
                                customer.wallet_names(currency)
                                while True:
                                    c_wallet_name = input("Type in wallet name you're sending from: ")
                                    if c_wallet_name in customer.wallets[currency].keys():
                                        break
                                    else:
                                        print('Input correct wallet name from list.')
                                r_email = input("Email address of Recipient: ")
                                recipient = customer_db.get_customer(r_email)
                                if recipient:
                                    recipient.wallet_names(currency)
                                    while True:
                                        r_wallet_name = input("Type in recipient's wallet name: ")
                                        if r_wallet_name in recipient.wallets[currency].keys():
                                            break
                                        else:
                                            print('Input correct wallet name from list.')
                                    amount = int(
                                        input("How much do you want to transfer: "))
                                    customer.get_wallet(currency, c_wallet_name).transfer(amount, recipient, r_wallet_name)
                                    break
                                else:
                                    print("Recipient not found.")
                            elif action == '5':
                                del_email = customer.email
                                customer.logout()
                                customer_db.delete_customer(del_email)
                                break
                            elif action == "0":
                                customer.logout()
                                break
                            else:
                                print("Wrong input. Try again.")
                elif u_type == "0":
                    login = False
                    break
                else:
                    print("Inappropriate Input. Try again.")
        elif log_or_sign == "2":
            f_name = input("Enter First Name: ")
            l_name = input("Enter Last Name: ")
            phone_no = input("Enter Phone Number: ")
            while True:
                acct = input(
                    "Enter 1 for Savings account. Enter 2 for Current Account: ")
                if acct == "1":
                    acct_type = "Savings"
                    break
                elif acct == "2":
                    acct_type = "Current"
                    break
                else:
                    print("Wrong Input")
            # validation for pin length and type
            while True:      
                pin = input("Please put in a secure 6-digit pin: ")
                if len(pin) == 6 and re.match("^(\d+)$", pin):
                    break
                else:
                    print("Enter a valid 6-digit pin.")
            # validation for email
            while True:
                email = input("Please input your email: ")
                if re.match("^([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6})*$", email):
                    break
                else:
                    print("Enter a valid email address, please.")
            print("Creating customer profile...")
            time.sleep(2)
            customer = Customer(f_name, l_name, phone_no,
                                acct_type, pin, email)
            customer_db.add_customer(customer)
            print("Your account has been created. Go ahead and login to create a wallet")
            break

        elif log_or_sign == "0":
            app_state = False
            with open('customer_db.pickle', 'wb') as file:
                pickle.dump(customer_db, file)
            
            with open('staff_db.pickle', 'wb') as file:
                pickle.dump(staff_db, file)

            break
        else:
            print("Wrong Input. Try again.")
            break