# Write a program to find the greatest of 3 numbers entered by the user.
num1 = int(input("Enter 3 numbers : "))
num2 = int(input())
num3 = int(input())
if(num1 > num2):
    if(num1 > num3):
        print(num1,"is bigger")
if(num3 > num2):
    print(num3,"is bigger")
else:
    print(num2,"is bigger")
