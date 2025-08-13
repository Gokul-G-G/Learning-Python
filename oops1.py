# Create student class that takes names and marks of three subjects as arguments in constructor
# Then create a method to print the average
 
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():
        print("Hello,Welcome")

    def average_mark(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi,",self.name,"Your average marks is ",sum/3)
    
s1 = Student("Gokul",[50,56,56])
s1.average_mark()
s1.hello()

# Constructor invoke when creating an object

# All classes have a function called __init__(),which is always executed when the object is being initiated.



########################
#  STATIC METHOS
########################

# Methods that don't use the self parameter (works at class level)

# class Student:
#     @staticmethod    #it is called decorator
#     def college():
#         print("My college")



######################
# ABSTRACTION AND ENCAPSULATION
######################
# ABSTRACTION
# Hiding the implementation details of a class and only showing the essential features to the user called abstraction.

# ENCAPSULATION
# Wrapping data and functions into a single unit (Object)