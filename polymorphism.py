# print(1+3)
# print("1"+"3")
# print(len("jenny"))
# l1=["jenny",7]
# print(len(l1))

# dict1={1:"jenny",2:"payal",3:"jiya"}
# print(len(dict1))

# DUCK TYPING to implement polymorphism

# def square(x):
#     return x*x
# print(square(5))
class Duck:
    def swim(self):
        print('i am a duck and i can swim')
    def speaks(self):
        print('Quack Quack')
class Dog:
    def swim(self):
        print('i am a dog and i can swim')
    def speaks(self):
        print("woof woof")
class person:
    def speaks(self):
        print("blah blah blah")
    def swim(self):
        print('i can swim')
class Demo:              
    def display(self,duck):
        duck.swim()
        duck.speaks()
        print('information displayed')
duck=Duck()
dog=Dog()
p=person()
demo=Demo()
demo.display(dog)
demo. display(duck)
demo.display(p)



 