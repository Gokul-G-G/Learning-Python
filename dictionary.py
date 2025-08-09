# store following word meanings in a python dictionary:
# table:"a piece of furniture","list of facts & figures"
# cat:"a small animal"

"""dict = {
    "table":["a piece of furniture","list of facts & figures"],
    "cat":"a small animal"
}

print(dict)"""


# You are given a list of subjects for students.Assume one classroom is required for 1 subject.
# How many classrooms are needed by all students.
 
"""subjects = {
    "python","java","C++","python","javascript","java","python","java","C++","C"
    }
print(subjects)
"""

# Write a program to enter marks of 3 subjects from the user and store them
# in a dictionary.Start with an empty dictionary and add one by one.Use subject 
# name as key and marks as value.

"""markList = {}
mark = int(input("enter the mark of physics: "))
markList.update({"physics":mark})
mark = int(input("enter the mark of chemistry: "))
markList.update({"chemistry":mark})
mark = int(input("enter the mark of biology : "))
markList.update({"biology":mark})
 
print(markList)"""

# Figure out a way to store 9 & 9.0 as seperate values in the set.
# (You can take help of built in data types)

values = {
  ("float",9.0),
  ("int",9)
}

print(values)