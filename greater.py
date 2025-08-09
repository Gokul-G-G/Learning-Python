# Write a program to find the greatest of 3 numbers entered by the user.
num1 = int(input("Enter 3 numbers : "))
num2 = int(input())
num3 = int(input())
if(num1 > num2 and num1 > num3):
    print("Number first is bigger",num1)
elif(num3 > num2):
    print("Number third is bigger",num3)
else:
    print("Number second is bigger",num2)
 