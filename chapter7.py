#function & recurrsion
# function definition
def avg ():
    a =int(input("enter your number:"))
    b=int(input("enter your number: "))
    c=int(input("enter your number:"))

    average =(a+b+c)/3
    print(average)
avg()#fuction call
print("thank you!")
avg()
print("thank you!")
avg()
print("thank you!")
avg()
avg()
def goodDay():
    print("good day")
goodDay()    
#function argument ..
def goodDay(name,ending):
    print("good Day,"+name)
    print(ending)
    return 7
    
a=goodDay("harry","thank you")
goodDay("rohan","thank you")
print(a)

