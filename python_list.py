number=[10,0,-1,7,-1]
names=['jenny','krishna','ram']
mix_list=[1,"jenny",10.5,True]
print(names)
print(mix_list)
print(number)
print(number[1]) # access the element of list
print(len(number)) # function
print(number[-2]) # negative index
print(number[0:4]) # slicing
print(number[1:])
print(number[:5])
print(number[0:5:2])
number.sort() #function
print(number)
number.reverse() # function
print(min(number)) # function
print(number)
#mix_list.sort()
print(mix_list)
number.append(45) # method at the end of list only one data
number.insert(2,45)
number.extend([34,89,56,45]) # at the end of the list more than one data.
number[1]=45
number[1:4]=[45,67,89]
number.remove(-1) # remove the first occurence of 0
number.pop()
print(number.pop())
print(number.pop(1)) # pass the index
print(number)

