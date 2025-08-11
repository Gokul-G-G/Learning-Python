# 1. print numbers from 1 to 100
"""count = 1
while count <= 100 :
    print(count)
    count += 1
print("Ended")"""

# 2. print numbers from 100 to 1

"""count = 100
while count >= 1:
    print(count)
    count -= 1
print("End")"""

# 3. Print the multiplication table of a number n

"""num = int(input("Which numbers multiplication table u want: "))
count = 1
while count <= 10:
    print(count,"x",num,"=",num*count)
    count +=1
print("Above shows the multiplication table of", num)"""

# 4. Print the elements of the following list using a loop:
# [1,4,9,16,25,36,49,64,81,100]

"""count = 1
list = []
while count <= 10:
    square = count * count
    list.append(square)
    count += 1
print("The List is",list)"""

# nums = [1,4,9,16,25,36,49,64,81,100]
# idx = 0
# while idx < len(nums):
#     print(nums[idx])
#     idx += 1

# 5. Search for a number x in this tuple using loop:
# (1,4,.9,,16,25,36,49,64,81,100)

"""tup = (1,4,9,16,25,36,49,64,81,100)
count = 0
check = int(input("Enter the number to check: "))
while count < len(tup):
    if(check == tup[count]):
        print(check,"present in index",count) 
        break
    else:
        print("Finding...")   
    count += 1
"""