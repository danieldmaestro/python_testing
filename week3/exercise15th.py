number = input("Enter a five-digit number: ")

def is_palindrome(number):
    e = len(number) + 1
    num = int(number)
    temp = num
    reverse = 0
    for n in range(1,e):
        digit = (num % 10**n)//10**(n-1)
        reverse += digit * 10**(5-n)
    if reverse == temp:
        print(temp, "is a palindrome.")
    else:
        print(temp, "is not a palindrome.")

is_palindrome(number)