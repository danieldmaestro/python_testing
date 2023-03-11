import datetime
current_time = datetime.datetime.now()

ats_backend = {
    "DanielM" : {
        "first_name" : "Daniel",
        "last_name" : "Momodu",
        "birth_date":"16th",
        "birth_month" : "October",
        "attendance": 0,
        "height" : 1.93,
        "weight" : 100,
        "age" : 24
    },
    "BusolaA" : {
        "first_name" : "Busola",
        "last_name" : "Adeyeye",
        "birth_date":"22nd",
        "birth_month" : "February",
        "attendance": 0,
        "height" : 1.53,
        "weight" : 60,
        "age" : 24
    },
    "AfolabiA" : {
        "first_name" : "Afolabi",
        "last_name" : "Adepena",
        "birth_date":"10th",
        "birth_month" : "February",
        "attendance": 0,
        "height" : 1.63,
        "weight" : 64,
        "age" : 25
    },
    "TaofeeqO" : {
        "first_name" : "Taofeeq",
        "last_name" : "Otu",
        "birth_date":"2nd",
        "birth_month" : "August",
        "attendance": 0,
        "height" : 1.67,
        "weight" : 78,
        "age" : 26
    },
    "FeranmiA" : {
        "first_name" : "Feranmi",
        "last_name" : "Akinyemi",
        "birth_date":"31st",
        "birth_month" : "August",
        "attendance": 0,
        "height" : 1.59,
        "weight" : 70,
        "age" : 27
    },
    "YetundeA" : {
        "first_name" : "Yetunde",
        "last_name" : "Alabi",
        "birth_date":"7th",
        "birth_month" : "January",
        "attendance": 0,
        "height" : 1.6,
        "weight" : 50,
        "age" : 28
    },
    "JafarB" : {
        "first_name" : "Jafar",
        "last_name" : "Busari",
        "birth_date":"26th",
        "birth_month" : "August",
        "attendance": 0,
        "height" : 1.73,
        "weight" : 67,
        "age" : 29
    }
}

# function to increment attendace by 1
def attendance_incre(initials):
    ats_backend[initials]["attendance"] += 1

attendance_incre("DanielM")

# function to update first name and last name
def name_update(initials, first_name, last_name):
    ats_backend[initials]['first_name'] = first_name
    ats_backend[initials]['last_name'] = last_name
    print(f"Student identified as {initials} has updated his name")

name_update("DanielM", "Daniel", "Maestro")

# function to return full name in title case
def full_name(initials):
    fname = ats_backend[initials]["first_name"]
    lname = ats_backend[initials]["last_name"]
    full_name = f"{fname} {lname}"
    # print("Full name is", full_name.title())
    return full_name.title()

# full_name("DanielM")

# function that adds new profile to class
def new_profile(fname, lname, bday, bmonth, height, weight, age):
    initials = f"{fname}{lname[:1]}"
    ats_backend[initials] = {}
    ats_backend[initials]["first_name"] = fname
    ats_backend[initials]["last_name"] = lname
    ats_backend[initials]["birth_date"] = bday
    ats_backend[initials]["birth_month"] = bmonth
    ats_backend[initials]["height"] = height
    ats_backend[initials]["weight"] = weight
    ats_backend[initials]["age"] = age
    # print("NEW PROFILE CREATED")

new_profile("Buju", "Benson", "20th", "August", 1.8, 88, 26)

# gets number of students in class
def student_count(class_dict):
    # print("Number of Students in class is", len(class_dict))
    return len(ats_backend)

student_count(ats_backend)

# to remove a profile
def delete_profile(initials):
    ats_backend.pop(initials)
    print("Profile deleted permanently!")

# delete_profile("JafarB")

# gets birth month
def get_birthmonth(initials):
    student = ats_backend[initials]
    fname = ats_backend[initials]["first_name"]
    bmonth = student["birth_month"]
    print(f"{fname}'s birth month is {bmonth} ")

get_birthmonth("DanielM")

# groups profile by birth month
def month_group():
    birth_months = list(set([i["birth_month"] for i in ats_backend.values()]))
    print(birth_months)
    for mnth in birth_months:
        month_grp = []
        for student in ats_backend.values():
            if student["birth_month"] == mnth:
                month_grp.append(student["first_name"])
        print("Students under the month of", mnth, ":", ", ".join(month_grp))
    # for student in ats_backend.values():
    #     month_group = []
    #     month = student['birth_month']
    #     if 
                    
# month_group("August")

# returns list of initals
def initials():
    initial_list = []
    for i in ats_backend.values():
        f_initial = i["first_name"][:1]
        l_initial = i["last_name"][:1]
        initial = f"{f_initial}{l_initial}"
        initial_list.append(initial)

    # print(initial_list)
    return initial_list

initials()

# returns BMI of a profile
def bmi_calc(initials):
    student = ats_backend[initials]
    name = student["first_name"]
    kg = student["weight"]
    m = student["height"]
    bmi = kg / m ** 2
    print(f"{name}'s BMI is {round(bmi,2)}")


# minimum age
def min_age():
    ages = [i["age"] for i in ats_backend.values()]
    print("The minimum age of the class is", min(ages))
    return min(ages)


# max age function
def max_age():
    ages = [i["age"] for i in ats_backend.values()]
    print("The max age of the class is", max(ages))
    return max(ages)


# the average age of the class
def avg_age():
    ages = [i["age"] for i in ats_backend.values()]
    avg = sum(ages) / len(ages)
    print(f"The average age is {int(avg)}")
    return int(avg)


# prints the birth year of a profile
def birth_year(initials):
    student = ats_backend[initials]
    name = student["first_name"]
    b_year = current_time.year - student["age"]
    print(f"{name}'s birth year is {b_year}")

# birth_year("DanielM")

print("   ")
print("   ")
print("   ")
print("CLASS DESCRIPTION")

# names = [full_name(name) for name in ats_backend.keys()]
# names_str = "\n".join(names)
# print(f"This is a class of {student_count(ats_backend)} students. The full name of the students in the class are as follows: ")
# print(names_str)
# min_age()
# max_age()
# avg_age()
# [bmi_calc(initial) for initial in ats_backend.keys()]
# birth_months = list(set([i["birth_month"] for i in ats_backend.values()]))

# [birth_year(initials) for initials in ats_backend.keys()]
# print("The initials for all students are:",  ", ".join(initials()))

month_group()










