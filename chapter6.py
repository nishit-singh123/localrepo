#LOOP
print(1)
print(2)
print(3)
print(4)
print(5)
#the same task can be done like this:
for i in  range(1, 6):#for loop
    print(i)
#while loop
i=1
while(i<41):
    print(i)
    i+=1    
#list using loop
l=[1,"harry",False,"this","rohan","shubham","shubhi"]
i=0
while(i<len(l)):
    print(l[i])
    i+=1
# iteration in list 
l=[1,4,6,234,6]
for i in l:
    print(i)
#iteration tupple
t=(1,7,'ROHAN',"sauraV")
for i in t:
    print(i)
#iteration in string
s="harry"
for i in s:
    print(i)
#for loop with else
l=[1,5,8,9,4]
for item in l:
    print(item)
else:
    print("done")#this is printed when the loop exhausts
#break concept
for i in range(100):
    if(i==34):
        break#exit the loop right now
    print(i)
#continue concept
for i in range(100):
    if(i==34):
        continue#skip this iteration
    print(i)
#pass concept
for i in range (654):
    pass
i=0
while(i<45):
    print(i)
    i+=1    
#practice set
#write a program to print multiplication of given number using for loop.
n=int(input("enter a number:"))
for i in range(1,11):
    print(f"{n}*{i}={n*i}")
#write a program to get all the names stored in a list"l" and which starts wiyh s.
l=["Harry","Sachin","Soham","Rahul"]
for name in l:
    if(name.startswith("S")):
        print(f"hello{name}")
#attempt problem 1 using while loop.
n=int(input("enter a number:"))
i=1
while(i<11):
    print(f"{n}*{i}={n* i}")
    i+=1 
#write a program to find whether a given number is prime or not.
n=int(input("enter:"))
for i in range(2,n):
    if (n%i)==0:
        print("number is not prime")
        break
else:
    print("number is a prime number")    
#write a program to find the sum of first n natural number using while loop.
n=int(input("enter a number:"))
i=0
sum=0
while(i<=n):
    sum +=i
    i+=1
print(sum)
#write a program to calculate the factorial of a given number using for loop.
n=int(input("enter the number:"))
product =1
for i in range(1,n+1):
    product=product*i
print(f"the factorial of {n} is {product}")
#write a program to print the following star pattern.
n=int(input("enter the number:"))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    print("*"*(2*i-1),end=" ")
    print ("")
#write a program to print the following star pattern.
n=int(input("enter the number:"))
for i in range(1,n+1):
    print("*"*i,end=" ")
    print ("")
#write a program to print the following star pattern.
n=int(input("enter the number:"))
for i in range(1,n+1):
    print("*"*i,end=" ")
    print ("")
#write a program to print the following star pattern.
n=int(input("enter the number:"))
for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"*n,end="")
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end=" ")
    print(" ")
#write a program to print multiplication table of n using for loops in reversed order.
n=input(input("enter the number:"))
for i in range (1,11):
    print(f"{n}*{11-i}={n*(11-i)}")


    
