# def welcome(name):
#     print(f"Welcome, {name}")


# welcome("Daniel")

# digit1 = int(input("Give me one digit: "))
# digit2 = int(input("Give me another digit: "))

# def calculator(x,y):
#     print(f"Addition equals {x + y}")
#     print(f"Subtraction equals {x - y}")
#     print(f"Multiplication equals {x * y}")
#     print(f"Division equals {x/y}")
#     print(f"Exponentiation equals {x**y}")

# calculator(digit1,digit2)

# def factor(x,y):
#     if x % y == 0:
#         print(y, "is a factor of", x)
#     else:
#         print(y, "is not a factor of", x)

# factor(15,3)

# def circle_calc(radius):
#     print(f"Perimeter of circle equals {2 * 3.142 * radius}")
#     print(f"Area of circle equals {3.142 * radius ** 2}")
#     print(f"Radius of circle equals {radius * 2}")


# circle_calc(15)

# def pass_check(username, password, _username, _password):
#     if _password != password or _username != username:
#         print("WRONG CREDENTIALS!!!")
#     else:
#         print("You have succesfully logged in.")

# username = input("Please input a username: ")
# password = input("Please input a new password: ")

# print("PLEASE LOGIN YOUR NEW ACCOUNT")

# _username = input("Please input your username to login: ")
# _password = input("Please input your password: ")

# # pass_check(username, password, _username, _password)

# # d = [1,2,3,4,5]

# # for i in range(0,len(d)):
# #     print(i)

# numbers = [1,2,10,5,7,8,4,15,20]

# numbers.append(9)
# # numbers.extend(54)

# numbers.sort()
# numbers.pop(2)
# numbers.remove(10)
# print(numbers)
# # for num in numbers:
#     if num % 2 == 0:
#         print(f"{num} is even")
#     else:
#         print(f"{num} is odd")

# def checker(number):
#     odd = 0
#     even = 0
#     for num in number:
#         if num % 2 == 0:
#             even += 1
#         else:
#             odd += 1
#     print(f"There are {odd} odd numbers and {even} even numbers")

# checker(numbers)
# write 

# import random

# subjects = ["Daniel", "Feranmi", "Peter Obi", "Gafar", "Yetunde", "Modupe", "Jonathan"]
# verb = ["going", "running", "riding", "walking", "voting", "listening", "cooking"]
# objects = ["home", "bike", "PDP", "chicken", "music", "company", "dog"]

# for i in range(15):
#     print(random.choice(subjects), random.choice(verb), random.choice(objects))
# l = [1,2,3,4,5]

# for num in l:
#     if num % 2 > 0:
#         continue
#     print(num)
import math

# def factor_check(number):
#     for num in range(1,number):
#         factors = []
#         factors.append(num)
#         for n in range(1,num):
#             if n > math.ceil(num/2):
#                 continue
#             elif num % n == 0:
#                 factors.append(n) 
#         print("Factors of", num, "are:", factors)

def factor_check(number):
    count = 0
    if number < 0:
        number = -number
    while count < number:
        factors = []
        count += 1
        count2 = 0
        while count2 < number:
            count2 += 1
            if count2 > math.ceil(number/2):
                continue
            elif count % count2 == 0:
                factors.append(count2)
            
    print(factors)


        

factor_check(-1056)


