import re

class User:
    def __init__(self, username:str, first_name:str, last_name:str, password:str):
        self._username = username #read_only
        self.__password = password #private
        self._first_name = first_name #public
        self._last_name = last_name #public
        self.is_loggedin = False #public

    @property
    def username(self):
        return self._username
    
    @property
    def password(self):
        return self.__password
    
    def change_first_name(self, new_fname):
        self._first_name = new_fname

    def change_last_name(self, new_lname):
        self._last_name = new_lname
    
    def change_username(self):
        """ Change Username"""
        while True:
            new_username = input("Input New Username: ")
            if new_username == self.username: 
                print("This username is thesame as your old username. Try something different.")
            else:
                self.__username = new_username
                break

    def change_password(self):
        """ Change Password. Input Old Username first. Password validation for security"""
        while True:
            current_password = input("Input your current password: ")
            if current_password == self.password:
                break
            else:
                print("Incorrect password! Try again.\n")
        while True:
            new_password = input("Password should have a minimum length of 6, at least 1 uppercase letter, at least 1 lowercase letter, at least 1 number and at least 1 special character.\nInput New Passowrd: ")
            if re.match('(?=^.{6,}$)((?=.*\w)(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[|!"$%&\/\(\)\?\^\'\\\+\-\*]))^.*', new_password):
                self.password = new_password
                print("Your password has been successfully reset.")
                break
            else:
                print("Input a more secure password.\n")

    def login(self):
        while True:
            username = input("Input your username: ")
            password = input("Input your password: ")
            
            if username == self.username and password == self.password:
                self.is_loggedin = True
                print("Successfully logged in.")
                break
            else:
                print("Wrong credentials. Try again")


class Admin(User):
    def __init__(self, username: str, first_name: str, last_name: str, password: str, mfa:int = 12345):
        super().__init__(username, first_name, last_name, password)
        self.__mfa = mfa

    def login(self):
        while True:
            username = input("Input your username: ")
            password = input("Input your password: ")
            mfa_code = int(input("Input your unique authentication code: "))
            
            if username == self.username and password == self.password and mfa_code == self.__mfa:
                self.is_loggedin = True
                print("Successfully logged in.")
                break
            else:
                print("Wrong credentials. Try again")
                # print(self.username)
                # print(self.password)
                # print(self.__mfa)
        

daniel = User('dmaestro', 'Daniel', 'Momodu', 'Danny01#')
admin_man = Admin('admin01', 'Taofeeq', 'Otu', 'Admin123#')

# daniel.login()
admin_man.login()

    
    
