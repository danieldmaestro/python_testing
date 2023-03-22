class Car:
    def __init__(self, doors):
        self.__doors = doors

    def add_door(self, value):
        self.__doors = value

    @property
    def door(self):
        return self.__doors


c = Car(4)
c.add_door(7)
print(c.door)