# from department import Department

class BasePerson:
    def __init__(self, first_name: str, last_name: str, email: str, dept):
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self.department = dept

    @property
    def first_name(self):
        return self._first_name
    
    @property
    def last_name(self):
        return self._last_name
    
    @property
    def email(self):
        return self._email
    
    @property
    def department(self):
        return self._department
    
    @department.setter
    def department(self, dept):
        self._department = dept

    # def __repr__(self) -> str:
    #     return self.first_name + " " + self.last_name
    
