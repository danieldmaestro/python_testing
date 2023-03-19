from customer import Customer
from staff import Staff
from wallet import Wallet
from admin import Admin
from customer_database import CustomerDatabase
from staff_database import StaffDatabase
import re
from csv import reader, writer
import pickle

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
    while login:
        if log_or_sign == "1":
            # while loop makes sure you're inputting valid queries
            while True:
                # input for choice of login. while loop to make sure correct input is put in
                u_type = input(
                    "LOGIN SCREEN\nChoose type of user\n\n1. ADMIN\n2. STAFF\n3. CUSTOMER\n0.MAIN MENU\n\nInput here: ")
                if u_type == "1":
                    #if admin, while loop to make sure of correct username and password 
                    while True:
                        username = input("Type in your username: ")
                        password = input("Type in your password: ")
                        # admin login method to validate username and password
                        admin.login(username, password)
                        if admin.is_loggedin:
                            break

                    while admin.is_loggedin:
                        while True:
                            # while loop to choose action for admin
                            action = input(
                                f"Welcome, {admin.f_name}.\nWhat do you want to do? Here are the inputs\n\n1. Create new Staff\n2. Suspend staff\n3. Remove staff from suspension\n4. View all staff and customer\n5. View all logs\n0.Log out\n\nInput here: ")
                            # CREATE STAFF
                            if action == "1":
                                f_name = input("Type in First Name: ")
                                l_name = input("Type in Last Name: ")
                                username = input("Type in Username: ")
                                admin.create_staff(f_name, l_name, username)
                                break
                            # SUSPEND STAFF 
                            elif action == "2":
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
                                with open("logs.csv") as file:
                                    reader_obj = reader(file)
                                    for row in reader_obj:
                                        if "user-class" not in row:
                                            print(" ".join(row))
                                break
                            elif action == "0":
                                admin.logout()
                                break
                            else:
                                print("Wrong Input. Try again.")
                # STAFF LOGIN
                elif u_type == "2":
                    while True:
                        username = input("Type in your username: ")
                        password = input("Type in your password: ")

                        staff = staff_db.get_staff(username)

                        staff.login(username, password)
                    
                        if staff.is_loggedin:
                            # changed default password on first login
                            if staff.default_p == "not_changed":
                                print(f"Dear, {staff.f_name}, please change your default password.")
                                new_pword = input("Type in new password: ")
                                staff.setpassword(new_pword)
                                break
                            else:
                                break
                                
                    while staff.is_loggedin:

                        while True:
                            action = input(
                                f"Welcome, {staff.f_name}.\nWhat do you want to do? Here are the inputs.\n\n1. View customer balance\n2. Take customer deposit\n0. Logout\n\nInput here: ")
                            if action == "1":
                                c_email = input("Customer Email Address: ")
                                customer = customer_db.get_customer(c_email)
                                if customer:
                                    customer.show_all_wallets()
                                    break
                                else:
                                    print("Customer not found.")
                                    break

                            elif action == "2":
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

                                    customer.wallet_names()
                                    while True:
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
                    while True:
                        email = input("Type in your email: ")
                        pin = input("Type in your pin: ")

                        customer = customer_db.get_customer(email)
                        if customer:
                            customer.login(email, pin)
                            if customer.is_loggedin:
                                break

                    while customer.is_loggedin:
                        while True:
                            action = input(
                                f"Welcome, {customer.f_name}.\nWhat do you want to do? Here are the inputs:\n\n1. Add New Wallet\n2. View Dashboard\n3. Make a withdrawal\n4. Make a transfer\n0. Logout.\n\nInput Here: ")
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
                                customer.wallet_names()
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
                                customer.wallet_names()
                                while True:
                                    c_wallet_name = input("Type in wallet name you're sending from: ")
                                    if wallet_name in recipient.wallets[currency].keys():
                                        break
                                    else:
                                        print('Input correct wallet name from list.')
                                r_email = input("Email address of Recipient: ")
                                recipient = customer_db.get_customer(r_email)
                                if recipient:
                                    recipient.wallet_names()
                                    while True:
                                        r_wallet_name = input("Type in recipient's wallet name: ")
                                        if wallet_name in recipient.wallets[currency].keys():
                                            break
                                        else:
                                            print('Input correct wallet name from list.')
                                    amount = int(
                                        input("How much do you want to transfer: "))
                                    customer.get_wallet(currency, c_wallet_name).transfer(amount, recipient, r_wallet_name)
                                    break
                                else:
                                    print("Recipient not found.")
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

            customer = Customer(f_name, l_name, phone_no,
                                acct_type, pin, email)
            print("Your account has been created. Go ahead and login to create a wallet")
            break

        elif log_or_sign == "0":
            app_state = False
            with open('customer_db.pickle', 'wb') as file:
                customer_db = pickle.dump(file)
            
            with open('staff_db.pickle', 'wb') as file:
                staff_db = pickle.dump(file)

            break
        else:
            print("Wrong Input. Try again.")
            break


