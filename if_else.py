height=int(input("enter your height in feet:"))
if height>=3:
    print("you can buy token")
    print("now you can board the metro")
    print("out of if block")    
else:
   print("No token required") #if else will be commented out then nothing wiil display from else if condition does not satisfy if condition.
print("out of if block")

#CODE EXERCISE

#check wether given number is even or odd.

number=int(input("enter the number:"))
if (number %2) ==0:
     print("this is even number. ")
else:
     print("this is odd number.") 

#NESTED

a=52
if a%2==0:
     print("even")
     if a>30:
          print("number is great than 30..great")
print("bye")

height=int(input("what is your height?"))
if height>=3:
     print("can ride")
     age=int(input("what is your age?"))
     if age<=12:
          print("please pay 50rs")
     elif age<=18:
          print("please pay 250rs")
     else:
          print("please pay 500 rs")           
          
else:
     print("can't ride")     
print("bye") 

#CODE EXERCISE

weight=float(input("enter your weight:"))
height=float(input("enter your height:"))
bmi=(weight/height**2)
if bmi<18.5:
     print(f"your bmi is{bmi} and you are underweight.")
elif bmi<25:
     print(f"your bmi{bmi} and you have a normal weight.")
elif bmi<30:
     print(f"your bmi is {bmi} and you are overweight")
elif bmi<35:
     print(f"your bmi is {bmi}and you are obese")
else:
     print(f"you are clinically obese") 

#CODE EXERCISE(MULTIPLE if statement)

height=int(input("what is your height?"))

if height>=3:
     print("can ride")
     age=int(input("what is your age?"))
     if age<12:
         bill=150
         print("ticket price is 150rs")
     elif age<=18:
          bill=200
          print('ticket price is 200rs.') 
     else:
          bill=300
          print("ticket price is 300.")
     want_photo=input("do you want to take photo(y/n)?")
     if( want_photo=='y'or'Y'):
          bill=bill+50
     print(f"your total bill is {bill}")     
else:
     print("can't ride")
print("good bye")

# CODING EXERCISE(pizz order program)

size=input("what size pizza you want(s/m/l):")
bill=0
if( size == "s"or size == "S"):
     bill =100
     print("small pizza price is 100rs. ")
elif (size =="M"or size=="m"):
     bill =200
     print("medium pizza price is 200rs")
else:
     bill =300
     print("large pizza price is 300rs.")
want_pepperoni=input("do you want to take pepperoni for pizza(y/n)")
if want_pepperoni=="y"or"Y":
   if( size =="s"or size=="S"):
     bill=bill+30
     print(f"your final bill is{bill}")
else:
    
     bill=bill+50
     print("your final bill is{bill}")
extra_cheese=input("do you want extra cheese(y/n)")
if extra_cheese=="y"or"Y":
    bill=bill+20     
print(f"your final bill is {bill}")

# CODE EXERCISE







                  

            
     