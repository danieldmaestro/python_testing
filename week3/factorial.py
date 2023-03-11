number = int(input("Find the factorial of: "))

def factorial(num):
    if num > 0:
        factorial = 1
        for n in range(1,num+1):
            factorial *= n

        # print("The factorial of", number, "is", factorial)
    else: 
        return None
    return factorial

factorial(number)


def calc_e(num):
    e = 1
    for x in range(1,num+1):
        e += 1/factorial(x)

    print(e)

calc_e(5)

def calc_pow_e(x):
    e = 0
    for n in range(0,x+1):
        e += (x**n)/factorial(n)

    print(e)

calc_pow_e(5)