# # PRINT FUNCTION

print()
print('First program-python print function')
print("it is declared like this:")
print('print("what to print")') 

# # STRING MANIPULATION

print("hello world\nhello world\n")
print("hello" +"world") # with no space , concatenation 
print("hello "+"world") # with space , after hello or before world or both.

# INPUT() FUNCTION IN PYTHON

input("what is your name?")
print("hello"+" jenny")
print("Hello"+" "+input("what is your name?")) # nested 
print("Hey"+" "+input("what is your name?")+","+"how are you")

# PYTHON VARIABLES

name=input("what is your name?")
length=len(name) # len() function
print(length)
name="jiya"
print(name)
a=1
b=' viaansh'
print(name+ b) # it is a type error not syntax if 'a' was there.

# SWAP TWO NUMBERS

a=input("no the value of a:")
b=input("no the value of b:")
temp=a
a=b
b=temp
print("a="+a)# we can use "," also in the place of "+".

# DATA TYPES

VAR_1=12345678943146778076654433
print(VAR_1)
var_2=123
var_3=10.1
print(var_2+var_3)
print(type(var_2))
print(type(var_3))
var_4=0o123
var_5=0x123
print(var_4)
print(var_5)
print(type(var_4))
print(type(var_5))
name= "jenny khatri" # string
print(type(name))
print(name[3]) # we can subscript here that is access character from index
name_1="nishit "
name_2="cs student"
name_3="123"
name_4="456"
a=4
print(5*"jenny\'s \\n \"lectures\"")# skip sequence
var=True # small't' is name eror.
a=1
b=2
var=a<b
print(var)
print(type(var))

# TYPE CASTING

print(len("12345")) # only string having len()function.
length=len("nishit singh")
print("your name has"+str(length) +"character") # type casting or type conversion.
new_length=str(length)
print(type(new_length))
a="10"
b="12"
print(int("10")+int("12"))
print(10+float("10"))
name="123" # it should not be "nishit" not having base 10
print(10+int(name))
first_number=input("enter first number:")
second_number=input("enter second number:")
sum=int(first_number)+int(second_number)
print(sum)

# CODING EXERCISES

number=input()
first_number=number[0]
second_number=number[1]
print(int(first_number)+int(second_number))

# OPERATORS IN PYTHON
# ARITHMETIC OPERATORS

print(4**2) # it is 4 to power of 2.
print(4+5)
print(6*4)
print(4/2)
print(4//2) # floor division 
print(5%2)
print(5+2*3-1+10/5) # precedence and associative rule
weight=int(input("enter the the weight in kg:"))
height=float(input("enter the height in metres:"))
calculate_BMI=weight/(height*height)
print("IT IS BODY MASS INDEX: "+calculate_BMI)

# ASSIGNMENT AND RELATIONAL OPERATORS

a,b,c=5,4,7
d=a+b+c #16
a+=3 #8
b+=4 #8
c+=5 #12
d//=a
print(a,b,c,d) #24
print(a==8) # relational
print(a<=5)
print(a!=6)
print(a<56)
print(a>1)
print((a+1)!=6)

# LOGICAL OPERATORS

a,b=4,3
print(a<3 or b==3)
print(not(b))
c=True
print(not(c))
print(a<=4 or c)

# BITWISE OPERATORS

a,b=5,4
print(a&b)
print(a|b)
print(a^b)
print(~b)
print(a>>2)
print(a<<2)

# IDENTITY OPERATORS

a=5
b='5' # if only 5 is written then it will be true.
print(a is not b)
print(id(a))
print(id(b))
a=5
print(id(a))
a=6.0
print(id(a))

# MEMBERSHIP OPERATORS

str='jenny khatri'
print('j'in str)
print('Jenny'in str)
print('jennykhatri'in str)
print('jenny khatri' in str)
print('jenny'not in str)
l1=[2,4,8,-9,-10]
print(2 in l1)
print(2 not in l1)

# CODING EXERCISE

weight=input('Enter weight in kg:')
height=input('Enter height in meter:')
bmi=int(weight)/float(height)**2
print(int(bmi))


















