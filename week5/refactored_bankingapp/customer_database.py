class CustomerDatabase:
    def __init__(self):
        self._customers = {

        }

    def add_customer(self, customer):
        self._customers[customer.email] = customer

    def get_customer(self, customer_email):
        return self._customers[customer_email]