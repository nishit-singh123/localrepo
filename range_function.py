a=range(-1,-10,-1) #sequence not occuring here sometimes 
print(a[4])
for i in a:
    print(i)
a=range(10,0)# here starting point is 0 and step size must be 1 so, it shoud be 11.print null
total=0
for i in range(1,101):
    total+=i
print(total)
total=0
for i in range(2,101,2):
    #if i%2==0:
    total=total+i
        
print(total) 
for number in range(1,16):
    if number%3==0 and number%5==0:
        print('fizzBuzz')
    elif number%3==0:
        print('Fizz')
    elif number%5==0:
        print('buzz')
    else:
        print(number)                           