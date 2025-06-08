# method overloading
class Demo:
    def add(self,*args):
        total=0
        for i in args:
            total=total+i
        return total    
    # def add(self,a,b,c=0):
    #     return a+b+c
d=Demo()
print(d.add(2,3))
print(d.add(1,2,3))
print(d.add(3,4,5,67,7,8)) 

# method overrriding

class Father:
    def sleep(self):
        print('sleeps from 10:00 pm to 5:00 am')
    def eat(self):
        print('eating')
class Son(Father):
    print("sleeps from 2:00 am to 10:00 am")
Ram=Son()
Ram.sleep()        

