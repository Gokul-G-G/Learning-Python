# WAP to find the sum of first n numbers. using while loop
# counter = 1
# sum = 0
# n = int(input("Enter the range: "))
# while counter <= n:
#     sum += counter
#     counter += 1
# print("Sum of the",n,"numbers is",sum)


# WAP to find the factorial of first n numbers. using for loop.

num = int(input("Enter the number to find Factorial: "))
fact = 1
for i in range(1,num+1):
    fact *= i
print("Factorial of",num,"is",fact)