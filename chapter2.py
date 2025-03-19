# STRING-indexing
name = "nishit"
nameshort =name[0:3]#start from index 0 all the way till 3 (excluding 3).
print(nameshort)
character1=name[1]
print(character1)
# slicing(negative and positive)
print(name[-4:-1])
print(name[1:4])
print(name[:4])
print(name[1:])#same as print(name[1:5])
#slicing with skip value
print(name[1:2:4])
#string function
print(len(name))
print(name.endswith("hit"))
print(name.startswith("ni"))
print(name.capitalize())
#escape_ sequence character
a="nishit is a \t very \n good \"boy\""
print(a)
#practice set
# write a python program to display a user entered name folowed by Good Afternoon using input()function.
name = input("enter your name:")
print(f"good afternoon,{name}")  

