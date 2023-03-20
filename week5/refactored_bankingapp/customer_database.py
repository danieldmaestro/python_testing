import time
class CustomerDatabase:
    def __init__(self):
        self._customers = {

        }

    def add_customer(self, customer):
        self._customers[customer.email] = customer

    def get_customer(self, customer_email):
        print("Getting customer...")
        time.sleep(1)
        if customer_email in self._customers.keys():
            return self._customers[customer_email]
        else:
            print("Customer not found!!Try again.")
            return None
    
    def all_customers(self):
        for customer in self._customers.values():
            print("->", customer)

    def delete_customer(self, customer_email):
        if customer_email in self._customers.keys():
            self._customers.pop(customer_email)
            print("Your account has been deleted permanently!")
