# import os

# Specify the directory path
# directory_path = '/'

# try:
    # Get the list of all entries in the directory
# entries = os.listdir(directory_path)
    
#     print(f"Contents of '{directory_path}':")
#     for entry in entries:
#         print(entry)
# except FileNotFoundError:
#     print(f"The directory '{directory_path}' does not exist.")
# except PermissionError:
#     print(f"Permission denied to access '{directory_path}'.")
# except Exception as e:
# print(f"An error occurred: {e}")
# comparison operator
d=5==7
print(d)

# logical operator
e=True or False
print(e)
#Type casting and function 
a="harry"
t =type(a)
print(t)
#input()function
a=int(input("enter number 1"))
b=int(input("enter number 2"))
print("number a is:",a)
print("number b is:",b)
print("sum is",a+b)
#write a python program to add two numbers.
a=34
b=45
print(a+b)
#write a python program to find remainder when a number is divided by z.
a=34
b=5
print("remainder when a is divided by b is ",a%b)
# check the type of variable assigned using input()function.
a=input("enter the value of a")
print(type(a))
# use camparision operator to find out whether a given variable a is given is greater than 'b' or not.Take a =34 and b=80.
a=int(input("enter number 1:"))
b=int(input("enter  number2:"))
print("a is greater than b is",a>b)
# write a python program to find an average of two numbers entered by he user.
a=int(input("enter a number 1:"))
b=int(input("enter a number 2:"))
print("average of these two number is ",(a+b)/2)
# wite a program to find out the square of two number.
a=34
b=89
print("square of these number is:",a*a,b*b)