class Department:
    def __init__(self, name:str, students:dict={}, lecturers:dict = {}, courses:list=[]):
        self._name = name
        self._students = students
        self._lecturers = lecturers
        self._courses = courses

    @property
    def name(self):
        return self._name
    
    @property
    def students(self):
        return self._students
    
    def add_student(self, student):
        self.students[student.first_name] = student

    def remove_student(self, student):
        self.students.remove(student)

    def get_student(self, std_first_name):
        return self.students.get(std_first_name)
    
    @property
    def lecturers(self):
        return self._lecturers
    
    def add_lecturer(self, lecturer):
        self.lecturers.update({lecturer.first_name: lecturer})

    def remove_lecturer(self, lecturer):
        self.lecturers.remove(lecturer)      

    @property
    def courses(self):
        return self._courses
    
    def add_courses(self, course):
        self.courses.append(course)

    def remove_course(self, course):
        self.courses.remove(course)
    
    def __repr__(self) -> str:
        return (f"Department of {self.name}\nSTUDENTS: {[student.first_name for student in self.students.values()]}\nLECTURERS: {[lecturer.first_name for lecturer in self.lecturers.values()]}\nCOURSES: {self.courses}")

