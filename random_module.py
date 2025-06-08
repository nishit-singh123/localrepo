import random
a=random.randint(1,3)
a=random.randrange(1,3)
a=random.random()
print(a)
a=random.uniform(1,3)
print(a)
l=[2,7,-7,8,98,45]
a=random.choice(l)
random.shuffle(l)
print(l)

#CODE EXERCISE

import random
names=input("Enter everybody's name separated by commas:")
names_list=names.split(",")
print(names_list)
length=len(names_list)
random_choice=random.randint(0,length-1)
random_choice=random.choice(names_list)
print(f"{random.choice(names_list)} will pay the bill")

#CODING EXERCISE(heads or tail)

import random
side=random.randint(0,1)
print(side)
if side==1:
    print("Heads")
else: 
    print("Tails")  
















  

