# full_name = input("What is your full name? ")
# age = input("What is your age? ")
# gender = input("What is your gender? ")
# complexion = input("What is your complexion? ")
# hometown = input("Where is your hometown? ")
# interests = input("What are your interests? ")
# ss_school_attended = input("Secondary School attended: ")
# ss_school_year = input("Year Graduated (Secondary School): ")
# uni_attended = input("What university did you attend? ")
# uni_year = input("Year Graduated(Uni): ")
# aspiration = input("Aspirations : ")


# print(f"My first name is {full_name.split()[0].capitalize()} and my last name is {full_name.split()[1].capitalize()}. I am {age} years old. My gender is {gender.capitalize()}. I am {complexion} in complexion. My hometown is {hometown.capitalize()}. I am interested in {interests}. I attended secondary school at {ss_school_attended.title()} and finished in the year {ss_school_year}. I attended university at {uni_attended.title()} and graduated in the year {uni_year}. My aspiration are to {aspiration}")

# nums = [1,2,3,4,5]

# num_multi = [num * 2 for num in nums]
# print(num_multi)

# num_100 = [num for num in range(1,101)]
# print(num_100)

# def combine_words(word, **kwargs):
#     return kwargs["prefix"] + word

# runner= combine_words("child", prefix="man")
# print(runner)

# def calculate(**kwargs):
#     operation_lookup = {
#         'add': kwargs.get('first', 0) + kwargs.get('second', 0),
#         'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
#         'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
#         'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
#     }
#     is_float = kwargs.get('make_float', False)
#     operation_value = operation_lookup[kwargs.get('operation', '')]
#     if is_float:
#         final = "{} {}".format(kwargs.get('message','The result is'), float(operation_value))
#     else:
#         final = "{} {}".format(kwargs.get('message','The result is'), int(operation_value))
#     return final

# import random

# arr = [1,2,3,4,5,6]
# # shuffled_arr = random.shuffle(arr)
# random.shuffle(arr)

# print(arr)