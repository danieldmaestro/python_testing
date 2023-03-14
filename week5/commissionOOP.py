class CommissionEmployee:
    def __init__(self, first_name, last_name, nin, gross_sales,commission_rate):
        self._first_name = first_name
        self._last_name = last_name
        self._nin = nin
        self.gross_sales = gross_sales
        self.commission_rate = commission_rate

    @property
    def first_name(self):
        return self._first_name
    
    @property
    def last_name(self):
        return self._last_name
    
    @property
    def nin(self):
        return self._nin
    
    @property
    def gross_sales(self):
        return self._gross_sales
    
    @gross_sales.setter
    def gross_sales(self, sales):
        if sales < float("0.00"):
            raise ValueError("Gross sales must be >= 0")
        
        self._gross_sales = sales

    @property
    def commission_rate(self):
        return self._commission_rate
    
    @commission_rate.setter
    def commission_rate(self, rate):
        if not (0.0 < rate < 1.0):
            raise ValueError("Interest rate must be greater than 0 but less than 1%")
        
        self._commission_rate = rate

    def earnings(self):
        return self.gross_sales * self.commission_rate
    
    def __repr__(self):
        return ('Commission Employee: ' + 
                f'{self.first_name} {self.last_name}\n' +
                f'National ID Number: {self.nin}\n' + 
                f'Gross sales: {self.gross_sales:.2f}\n' +
                f'Commission rate: {self.commission_rate:.2f}')


class SalariedCommissionEmployee(CommissionEmployee):
    def __init__(self, first_name, last_name, nin, gross_sales, commission_rate, base_salary):
        super().__init__(first_name, last_name, nin, gross_sales, commission_rate)
        self.base_salary = base_salary

    @property
    def base_salary(self):
        return self._base_salary
    
    @base_salary.setter
    def base_salary(self, salary):
        if salary < 0:
            raise ValueError("Salary must be >= 0")
        
        self._base_salary = salary

    def earnings(self):
        return super().earnings() + self.base_salary
    
    def __repr__(self):
        return ("Salaried" + super().__repr__() +
                f"\nBase Salary: {self.base_salary:.2f}")

s = SalariedCommissionEmployee("Daniel", "Maestro", "223457890", 1122000.40, 0.09, -4)
c = CommissionEmployee("Busola", "Adeyeye", "225657890", 1122000.40, 0.09)

# employees = [c,s]

# for employee in employees:
#     print(employee)
#     print(f"{employee.earnings():,.2f}\n")
# print(c)
# print(s)
# print(f"{c.earnings():,.3f}")
# print(f"{s.earnings():,.3f}")