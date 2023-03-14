from department import Department
from baseperson import BasePerson


class Student(BasePerson):
    # student class inherits from baseperson class 
    def __init__(self, first_name:str, last_name:str, email:str, dept:Department, student_Id:int, courses:dict={}):
        super().__init__(first_name, last_name, email, dept)
        self._student_Id = student_Id
        self._courses = courses
    # add new properties - studentID and courses
    @property
    def student_Id(self):
        return self._student_Id
    
    @property
    def courses(self):
        if self._courses == {}:
             print("No courses registered yet.")
        else:
            return self._courses
    # courses setter property
    @courses.setter
    def courses(self, new_course):
        if isinstance(new_course, Course):
            self._courses[new_course.course_code] = new_course
        else:
            raise TypeError("This course is not a Course object")

    def register_course(self, course):
        self.courses = course

    def remove_course(self, course):
        self.courses.remove(course)

    def get_course(self, course_code):
        return self.courses[course_code]
    
    def __repr__(self) -> str:
        return (f"NAME: {self.first_name} {self.last_name}\nSTUDENT ID: {self.student_Id}\nDEPARTMENT: {self.department.name}\nCOURSES OFFERED: {[course for course in self.courses.values()]}")

    
class Lecturer(BasePerson):
    # lecturer inherits from baseperson class
    def __init__(self, first_name:str, last_name:str, email:str, dept, lecturer_Id:int):
        super().__init__(first_name, last_name, email, dept)
        self._lecturer_Id = lecturer_Id

    @property
    def lecturer_Id(self):
        return self._lecturer_Id
    # lecturer can set score of student
    def set_score(self, student, score, course_code):
        student.courses[course_code].score = score

    def __repr__(self):
        return (f"NAME: {self.first_name} {self.last_name}\nLECTURER ID: {self.lecturer_Id}\nDEPARTMENT: {self.department.name}")

class Course:
    def __init__(self, title:str, course_code:str, credit_load:int, lecturer, score:int = 0):
        self._title = title
        self._course_code = course_code
        self._credit_load = credit_load
        self._lecturer = lecturer
        self.score = score

    @property
    def title(self):
        return self._title
    
    @property
    def course_code(self):
        return self._course_code
    
    @property
    def credit_load(self):
        return self._credit_load
    
    @property
    def lecturer(self):
        return self._lecturer
    
    @lecturer.setter
    def lecturer(self, lect):
        if isinstance(lect, Lecturer):
            self._lecturer = lect
        else:
            raise ValueError("Lecturer isn't an instance of the Lecturer class.")
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        if value > 100 or value < 0:
            raise ValueError("Value must be within 0 and 100")
        
        self._score = value
    
    @property
    def grade(self):
        if self.score < 50:
            return 'F'
        elif 50 <= self._score < 60:
            return 'D'
        elif 60 <= self._score < 70:
            return 'C'
        elif 70 <= self._score < 80:
            return 'B'
        else:
            return 'A'
    
    def __repr__(self) -> str:
        return self.course_code


csc = Department("Computer Science")
habeeb = Lecturer("Habeeb", "Habeeb", "habeeb@gmail.com", csc, 2345)
ridwan = Lecturer("Ridwan", "Ridwan", "ridwan@gmail.com", csc, 2346)
csc110 = Course("Intro to Computing", "CSC110", 3, habeeb)
css212 = Course("Intro to CSS", "CSS212", 3, ridwan)
pyt110 = Course("Intro to Python", "PYT110", 4, habeeb)
djg110 = Course("Intro to Django Framework", "DJG110", 4, habeeb)
feranmi = Student("Feranmi", "Akinyemi", "feranmi@gmail.com", csc, 1234,{})
daniel = Student("Daniel", "Momodu", "daniel@gmail.com", csc, 1235,{})

feranmi.register_course(csc110)
feranmi.register_course(css212)
daniel.register_course(css212)
daniel.register_course(csc110)
daniel.register_course(djg110)

# print(csc.lecturers)
csc.add_lecturer(habeeb)
csc.add_lecturer(ridwan)
csc.add_student(feranmi)
csc.add_student(daniel)
# print(csc)

csc.add_courses(csc110)
csc.add_courses(css212)
csc.add_courses(djg110)
csc.add_courses(pyt110)

# csc.add_student(daniel)
# print(feranmi.courses['CSS212'].title)
# feranmi.register_course(pyt110)
print(feranmi)
print("\n")
print(daniel)
print("\n")
print(habeeb)
print("\n")
print(ridwan)
print('\n')
print(csc)

# habeeb.set_score(feranmi, 90, 'PYT110')
# print(feranmi.courses['PYT110'].grade)


# feranmi.courses = pyt110
# feranmi.courses[1].score = 109
# print(feranmi.courses[1].score)
