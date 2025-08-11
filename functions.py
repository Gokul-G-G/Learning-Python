# Write a function to print the length of a list.(list is the parameter)

# def cal_length(list):
#     print(len(list))

# cal_length([1,2,3,2,4])


# Write to print the elements of a list in sigle line.(list the parameter)

# def print_len(list):
#     for item in list:
#         print(item, end=" ")

# print_len(["orange","apple","mango","kivi"])

# Write to find the factorial of n.


# def cal_fact(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#     print(fact)

# cal_fact(5)

# Write a program to convert USD to INR

# def convert(usd_val):
#     inr_val = usd_val * 87.67
#     print(usd_val,"USD =",inr_val, "INR")

# convert(2)


# write a function will get a number and check the number is even or odd

# def num_check(num):
#     if(num % 2 == 0):
#         print("Even")
#     else:
#         print("Odd")

# num_check(4)



#####################
# RECURSION
######################

# def show(n):
#     if(n == 5): #Base case
#         return
#     print(n)
#     show(n+1)

# show(1)


# def sum(n):
#     if(n == 1):
#         return 1
#     return sum(n-1)+n

# print(sum(10))


# Write a recursive function to print all elements in a list.

def print_lis(list,idx):
    if(idx == len(list)):
        return
    print(list[idx])
    print_lis(list,idx+1)

cities = ["kochi","mumbai","chennai","delhi","noida "]
print_lis(cities,0)