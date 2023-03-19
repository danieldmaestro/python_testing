class StaffDatabase:
    def __init__(self):
        self._staffs = {

        }

    def add_staff(self, staff):
        self._staffs[staff.username] = staff

    def get_staff(self, staff_username):
        return self._staffs[staff_username]
    
    def all_staff(self):
        for staff in self._staffs.values():
            print(staff)