import datetime
current_time = datetime.datetime.now()

# list model
classroom_list = [
    ["Daniel", "Momodu", 1.93, 100, 1999, "Male"],
 ["Bradd", "Pitt", 1.47, 73, 1980, "Male"], 
 ["Bola", "Tinubu", 1.3, 66, 1960, "Male"], 
 ["Buhari", "Muhammadu", 1.6, 77, 1956, "Male"], 
 ["Hilary", "Clinton", 1.25, 67, 1973, "Female"]
 ]

# dictionary model
classroom_dict = {
    1 : {
        'first_name': "Daniel",
        'last_name' : "Momodu",
        'height' : 1.93,
        'weight' : 100,
        'birth_year' : 1999,
        'gender' : "Male"
    },
    2 : {
        'first_name': "Bradd",
        'last_name' : "Pitt",
        'height' : 1.47,
        'weight' : 73,
        'birth_year' : 1980,
        'gender' : "Male"
    },
    3 : {
        'first_name': "Bola",
        'last_name' : "Tinubu",
        'height' : 1.3,
        'weight' : 66,
        'birth_year' : 1960,
        'gender' : "Male"
    },
    4 : {
        'first_name': "Buhari",
        'last_name' : "Muhammadu",
        'height' : 1.6,
        'weight' : 77,
        'birth_year' : 1956,
        'gender' : "Male"
    },
    5 : {
        'first_name': "Hilary",
        'last_name' : "Clinton",
        'height' : 1.25,
        'weight' : 67,
        'birth_year' : 1973,
        'gender' : "Male"
    },
}

# tuple model
classroom_tuple = (
    ("Daniel", "Momodu", 1.93, 100, 1999, "Male"),
 ("Bradd", "Pitt", 1.47, 73, 1980, "Male"), 
 ("Bola", "Tinubu", 1.3, 66, 1960, "Male"), 
 ("Buhari", "Muhammadu", 1.6, 77, 1956, "Male"), 
 ("Hilary", "Clinton", 1.25, 67, 1973, "Female")
)

# function takes in individual student
def bmi_calc (student):
    # if block checks for data type of student
    if type(student) == list:
        bmi = student[3] / student[2] ** 2
        return bmi
    elif type(student) == dict:
        bmi = student["weight"] / student["height"] ** 2
        return bmi
    elif type(student) == tuple:
        bmi = student[3] / student[2] ** 2
        return bmi

# function takes in individual student
def age_calc (student):
    if type(student) == list:
        age = current_time.year - student[4]
        return age
    elif type(student) == dict:
        age = current_time.year - student["birth_year"]
        return age
    elif type(student) == tuple:
        age = current_time.year - student[4]
        return age
    

# print BMI for students in list model
print(f"BMI is {bmi_calc(classroom_list[0])}")
print(f"BMI is {bmi_calc(classroom_list[1])}")
print(f"BMI is {bmi_calc(classroom_list[2])}")
print(f"BMI is {bmi_calc(classroom_list[3])}")
print(f"BMI is {bmi_calc(classroom_list[4])}")

# print BMI for students in tuple model
print(f"BMI is {bmi_calc(classroom_tuple[0])}")
print(f"BMI is {bmi_calc(classroom_tuple[1])}")
print(f"BMI is {bmi_calc(classroom_tuple[2])}")
print(f"BMI is {bmi_calc(classroom_tuple[3])}")
print(f"BMI is {bmi_calc(classroom_tuple[4])}")

# print BMI for students in dictionary model
print(f" BMI is {bmi_calc(classroom_dict[1])}")
print(f" BMI is {bmi_calc(classroom_dict[2])}")
print(f" BMI is {bmi_calc(classroom_dict[3])}")
print(f" BMI is {bmi_calc(classroom_dict[4])}")
print(f" BMI is {bmi_calc(classroom_dict[5])}")

# print age for list model
print(f" AGE IS {age_calc(classroom_list[0])}")
print(f" AGE IS {age_calc(classroom_list[1])}")
print(f" AGE IS {age_calc(classroom_list[2])}")
print(f" AGE IS {age_calc(classroom_list[3])}")
print(f" AGE IS {age_calc(classroom_list[4])}")

# print age for tuple model
print(f" AGE IS {age_calc(classroom_tuple[0])}")
print(f" AGE IS {age_calc(classroom_tuple[1])}")
print(f" AGE IS {age_calc(classroom_tuple[2])}")
print(f" AGE IS {age_calc(classroom_tuple[3])}")
print(f" AGE IS {age_calc(classroom_tuple[4])}")

# print age for dictionary model
print(f" AGE IS {age_calc(classroom_dict[1])}")
print(age_calc(classroom_dict[2]))
print(f" AGE IS {age_calc(classroom_dict[3])}")
print(f" AGE IS {age_calc(classroom_dict[4])}")
print(f" AGE IS {age_calc(classroom_dict[5])}")

