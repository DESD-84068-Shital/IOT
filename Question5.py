"""5)The marks obtained by a student in 3 different subjects are input by the user. Your program should calc
ulate the average of subjects and display the grade. The student gets a grade as per the following rules:
Average Grade
90-100 A
80-89 B
70-79 C
60-69 D
0-59 F"""

m1=int(input("Enter marks of m1:"))
m2=int(input("Enter marks of m2:"))
m3=int(input("Enter marks of m3:"))

Avg=int((m1+m2+m3)/3)
print(f"Average={Avg}")

if Avg>=90 and Avg<100:
    print("Grade:A")

elif Avg>=80 and Avg<89:
    print("Grade:B")
    
elif Avg>=70 and Avg<79:
    print("Grade:C")

elif Avg>=60 and Avg<69:
    print("Grade:D")

elif Avg>=0 and Avg<59:
    print("Grade:F")

    