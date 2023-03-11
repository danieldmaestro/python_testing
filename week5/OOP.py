class Time:
    def __init__(self, seconds=0):
        self.seconds = seconds
        self.hour = self.seconds//3600
        self.minute = ((self.seconds)%3600)//60
        self.second = ((self.seconds)%3600)%60

    @property
    def hour(self):
        return self._hour
    
    @hour.setter
    def hour(self, hour):
        if not (0 <= hour < 24):
            raise ValueError("Seconds must be between 0 and 23")

        self._hour = hour

    @property
    def minute(self):
        return self._minute
    
    @minute.setter
    def minute(self, minute):
        if not (0 <= minute < 60):
            raise ValueError("Minute must be between 0 - 59")
        
        self._minute = minute
    
    @property
    def second(self):
        return self._second
    
    @second.setter
    def second(self, second):
        if not (0 <= second < 60):
            raise ValueError("Second must be between 0 - 59")
        
        self._second = second

    def set_time(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second


wakeup = Time(81003)

print(wakeup.hour)
print(wakeup.minute)
print(wakeup.second)
class PrivateClass:
    def __init__(self):
        self.public_data = "public"
        self.__private_data = "private"


my_object = PrivateClass()

print(my_object.public_data)
print(my_object.__private_data)



