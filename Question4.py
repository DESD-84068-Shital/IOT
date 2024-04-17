#4] Write a Python function to find the maximum of three numbers.

num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
num3=int(input("Enter number 3:"))

def max(num1,num2,num3):
    if (num1>num2) & (num1>num3):
        print(f"num1 is greater")

    elif num2>num3:
        print(f"num2 is greater")
        
    else:
        print("num3 is greater") 

max(num1,num2,num3)