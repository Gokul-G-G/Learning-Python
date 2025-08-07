# Conditional statements

# if-elif-else (SYNTAX)

""" if(condition):
        Statement1
    elif(condition):
        Statement2
    else:
        StatementN """

age = 10
if(age >= 18):     #INDENTATION is very important in python
    print("Vote")
elif(age<18):
    print("Under age")
else:
    print("Not Valid")


#TRAFFIC LIGHT
light=(input("light color: ")) #take input from the user
if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("look") 
else:
    print("light is broken")