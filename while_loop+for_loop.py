count=5
while count>0:
    print(count)
    count-=1
    if count==3:
      break 
else:
     print('in selse block ')
print("out from loop")
number=int(input("enter a number(-1 to quit)"))
while number!=-1: # it is a special value or sentimal value
    print(number)
    number +=1
    print(number)
    number=int(input("enter a number(-1 to quit)"))
else:
    print('in else block')
print('out from loop')
count=0
while True:
    print(count)
    count+=1
    if count==5:
        break
else:
    print('in else block')
print('out from loop')
total=0
number=int(input("enter a number(10 to quit):"))
while number!=10:
    total= total+number
    number=int(input("enter a number(10 to quit):"))
print("total is",total)

#FOR LOOP

name='jenny'
for i in name:
    print(i)
names=['jenny','Ram','Shyam']
for i in names:
    print(i)
    if i=='jenny':
        print('hey,it is me')
list1=[6,-8,6,78,3,9]
squares=[]
for i in list1:
    square=i**2
    squares.append(square)
print(squares)

#FOR ELSE IN PYTHON

tuple=(2,67,89,56,-9)
for i in tuple:
    print(i)
    if i % 6==0:
        break
    else:
        print(" there is no number in this group")
else:
    print('loop is successfully completed') # else block wiil no be executed because of break
print("out of for/else") 

#CODING EXERCISE

heights=input("enter all heights separated by space:")
heights_list=heights.split()
print(heights_list)
count=0
for height in heights_list:
    count=count+1
print(count)
for i in range(0,count):
    heights_list[i]=int(heights_list[i])
print(heights_list)
total=0
for height in heights_list:
    total=total+height
avg=total/count
print(round(avg))

# CODING EXERCISE

numbers=input('enter the number seperated by spaces:')
numbers_list=numbers.split()
print(numbers_list)
count=0
for i in numbers_list:
    count=count+1
for i in range(0,count):
    numbers_list[i]=int(numbers_list[i])
#print(numbers_list)
maximum_number=0
for number in numbers_list:
    if number>maximum_number:
        maximum_number=number
print(f"the maximum number is {maximum_number}")        




















