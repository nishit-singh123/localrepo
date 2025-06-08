#BREAK(LOOP CONTROL)

count=1
while count<=10:
    print(count)
    count+=1
    if count==7:
        break
    print("Hi")
print('out from loop')

#NESTED LOOP

list1=["Hi","Hello","Welcome"]
names=["krishna","Ram","Madhav"]
for item in list1:
    for name in names:
        print(item,name)
        if item=="hello"and names=="ram":
            break
    print("out from inner loop")
print("out from outer loop")

#CONTINUE (WHILE LOOP)

count=1
while count <=10:
    print(count)
    count+=1
    if count==7:
        continue
    print("Hi")
print('out fro loop')  

# CONTINUE (FOR LOOP)

for i in range(1,11):
    if i==7:
        continue
    
    else:
        print(i)
#PASS

for i in range(1,11):
    pass

# INDENTATION

for i in range(5):
 print("Hi") # this is a part of loop
 print("Jenny")
 if i==3:
  print('welcome')
  if True:
   print("namaste")
print("bye take care!")  











