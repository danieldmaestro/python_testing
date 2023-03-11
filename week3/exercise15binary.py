number = input("Enter binary number: ")

def dec_convert(number):
    exp = len(number) + 1
    num = int(number)
    decimal = 0
    for n in range(1,exp):
        binary = (num % 10**n)//10**(n-1)
        decimal += binary * 2**(n-1)
    print(num, "to base 10 is", decimal)

dec_convert(number)


