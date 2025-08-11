# 1. Print numbers from 1 to 100 using for & range()
"""for i in range(1,101):
    print(i)"""

# 2. Print numbers from 100 to 1 using for & range()
"""for i in range(100,0,-1):
    print(i)"""

# 3. Print the multiplication table of a number n
num = int(input("Which numbers multiplication table u want: "))
for i in range(1,11):
    print(i,"x",num,"=",i*num)