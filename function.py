def greet():
    print("Hi")
    print("Jenny")
greet()
greet()
greet()

# # FUNCTION WITH ARGUMENTS

def add(a,b):
    c=a+b
    print(f"sum is {c}")
add(5,6)
add(8,9)

# # TYPES OF ARGUMENTS

def greet(name, subject,dept='cs'):# default arguments
    print(f"hi {name}")
    print(f'do you teach{subject}')
    print(f"Are you from{dept} department")
greet("jenny","cs") # positional arguments
greet(dept="cs",name="jenny") # keyword arguments
greet("jenny",dept='cs') # MIXTURE OF BOTH
greet("jenny","python")

def add(*numbers):# arbitrary keyworded arguments
    c=0
    print(numbers[0])
    #numbers[0]=4 python are not mutable
    for i in numbers:
        c=c+i
    print(f"sum is {c}")
add(3,7,8,9)
add(9,8,6,4,7)
add(6,9,98,56,98)

def add(*numbers,name):# keyworded argument
    c=0
    print(name)
    print(numbers)
    # numbers[0]=4
    for i in numbers:
        c+=i
        print(f"sum is {c}")
add(1,3,4,name="jenny")

def info_person(*args,**kwargs):# keyworded
    for key,value in kwargs.items():
        print(key,value)
    print(args)     

info_person(1,3,name="ram",age=30,dept="CSE")
info_person(7,6,7,name="shyam",dept="CSE")

# # CODING EXERCISE

import math
def paint_calculation(width,height,cover):
    area=height*width
    no_of_cans=math.ceil(area/cover)
    print(f"you will need {no_of_cans} cans of paint.")
h=int(input('Enter the height of wall in metres:\n'))
w=int(input('Enter the width of wall in metres:\n'))
coverage=7    
paint_calculation(width=w,height=h,cover=coverage)


import math
def prime_checker(number):
    is_prime=True
    if number==1:
        is_prime==False
    for i in range(2,math.ceil(number)):
        if number%i==0:
            is_prime=False
    if is_prime:
        print('it is a prime number')
    else:
        print("not a prime number")
n=int(input("enter a number:\n"))
prime_checker(n)                        

# RETURN VALUE
 
def add(a,b):
    c=a+b
    #return
    return c
    #return a+b
    #print(c)
    #return(c)
#print(add(5,4))
result=add(5,4)
print(result)

def forrmatt_name(first_name,last_name):
    formatted_name1=first_name.title()
    formatted_name2=last_name.title()
    return(f'{formatted_name1},{formatted_name2}')




print(forrmatt_name('nishit','singh'))

# RETURN MULTIPLE VALUES

import statistics
def mean_median_mode(list1):
    return [statistics.mean(list1),statistics.median(list1),statistics.mode(list1)]
    print('end of function')


a,b,c=(mean_median_mode([3,5,45,3,2,1,89]))
print(f'Mean is {a}\nMedian is {b}\nMode is {c}')
def add (a,b):
    if a==0 & b==0:
        return ' you have entered zero for both variables.'
    else:
        return a+b
var1=int(input("enter first variable :\n"))
var2=int(input("enter second variable:\n"))
result=add(var1,var2)
print(result)

# CODING EXERCISE

def leap_year(year):
    if year % 4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        False
def days_in_month(year,month):
    days_list=[31,28,31,30,31,30,31,31,30,31,30,31]
    if leap_year(year) and month==2:
        return 29
    else:
        return days_list[month-1]
year=int(input("enter a year:"))
month=int(input("Enter a month:"))
days=days_in_month(year,month)
print(days)

#PRINT VS RETURN

def func1(x):
    return x+1
    
    print(x)
output=  func1(3,4)
print(output)

def func2(a,b):
    c=a+b
    return(c)
output=func2(3,4)
func1(output)
final_output=func1(output)
print(output)
print(final_output) 

# LOCAL VS GLOBAL SCOPE

a=10 # global
def display():
     #a=15 # local
     def show():
          print(a)
     show()
print(a)
display()
print(a)
 
# there is no block scope in python but only global and local scope only for function.

a,b=8,6
if a>b:
    c=a+b
print(c)

# GLOBAL KEYWORD
a=10
def display():
    a=20
    def show():
        global a
        a=30
        #a=a+1
    print(a)
    show()
    print(a)
display()
print(a)    





    

                    



