# Store your Name, Age, Weight, Whether you are a student or not 
# (True for yes, False for no) in respective variables. What do 
# you think is the data type of each variable? Print the data type 
# of every variable. Change the datatype of Age to string and Weight to an integer.

name = str(input("Enter your Name: "))
age = int(input("Enter your Age: "))
weight = float(input("Enter your weight: "))
student = True

print(type(name))
print(type(age))
print(type(weight))
print(type(student))

age = str(age)
weight = int(weight)