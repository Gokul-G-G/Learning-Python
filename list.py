# write a program to ask user to enter names of their 3 favorite movies and store them in a list.
"""mov = []
mov.append(input("Enter your 1st fav movie : "))
mov.append(input("Enter your 2nd fav movie : "))
mov.append(input("Enter your 3rd fav movie : "))
print(mov)"""


# write a program to check if a list contains a palindrome of elements (Hint: use copy()method)

"""list = [1,2,3,4,3,2,1]
listCopy = list.copy()
listCopy.reverse()
if( list == listCopy):
    print("Palindrome")
else:
    print("Not Palindrome")"""

# write a program to count the number of students with the "A" grade in the following tuple.
 
grade = ("C","D","A","A","B","B","A")

print(grade.count("A"))

# store the above values in a list & sort them from "A" to "D".

list = ["C","D","A","A","B","B","A"]
list.sort()
print(list)