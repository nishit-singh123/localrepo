#LIST&TUPPLE
friends=["apple","orange",5,345.06,False,"akash","rohan"]#list canbe indexed like string.
print(friends[0])
friends[0]="grapes"
print(friends[0])#list are mutable,unlike strings.
#list slicing
print(friends[1:4])
friends.append("harry")#method
print(friends)
l1=[1,7,9,3,6,]
l1.sort()#method
l1.reverse()
l1.insert(4,478898899)
l1.remove(7)
print(l1.pop(4))
print(l1)
#TUPPLES-IT IS ALSO NOT MUTABLE.
a=(1,3.8,False,"rohan","shivam")
print(type(a))
print(a)
#tupple method
a.count(3.8)
print(a.count(3.8))
print(a.index(False))
#tupple operation
b=(4,7,9)#repetition
result=a+b
print(result)#concatenation
print(b)
print(b[2:5])#slicing
print(9 in b)#membership
print(len(b))#tuple length
e,f,g= b
print(e,f,g)
#practice set
#write a program to store seven marks in a list entered by the user.
marks=[]
f1=int(input("enter marks here:"))
marks.append(f1)
f2=int(input("enter marks here:"))
marks.append(f2)
f3=int(input("enter marks here:"))
marks.append(f3)
f4=int(input("enter marks here:"))
marks.append(f4)
f5=int(input("enter marks here:"))
marks.append(f5)
f6=int(input("enter marks here:"))
marks.append(f6)
f7=int(input("enter marks here:"))
marks.append(f7)
f8=int(input("enter marks here:"))
marks.append(f8)
marks.sort()
print(marks)
#check that tupple type cannot be changed in python.
a=(34,45,"harry")
a[3]="larry"
#write a program to sum a list with 4 numbers.
n=[56,89,67,45]
print(sum(n))
#write a program to count the number of zeroes in the following tuple.
a=(7,0,8,0,0,9)
n=a.count(0)
print(n)









