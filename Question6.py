#6) Write a Python function to calculate the factorial of a number (a non-negative integer). The function acc
#epts the number as an argument.


def fact(num):
    i=1
    fact=1
    while i<=num:
        fact=fact*i
        i=i+1
    print(f"factorial={fact}")

num=int(input("Enter number:"))
fact(num)