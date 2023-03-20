import time
class StaffDatabase:
    def __init__(self):
        self._staffs = {

        }

    def add_staff(self, staff):
        self._staffs[staff.username] = staff

    def get_staff(self, staff_username):
        print("Getting staff...")
        time.sleep(1)
        if staff_username in self._staffs.keys():
            return self._staffs[staff_username]
        else:
            return None
    
    def all_staff(self):
        for staff in self._staffs.values():
            print("->", staff)