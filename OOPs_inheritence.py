class Human:
    def __init__(self):
        self.num_eyes=2
        self.num_nose=1
    def eat(self):
        print('i can eat')
    def work(self):
        print('i can work')
class Male(Human):
    # def __init__(self,name):
    #     super().__init__()
    #     self.name=name
        
    def flirts(self):
        print('i can flirts')
    def work(self):
        super().work()
        print('i can code')
male_1=Male('jenny')
male_1.flirts()
male_1.work()
print(male_1.num_eyes)
print(Male.mro())



# MULTIPLE INHERITENCE
class Human:
    def __init__(self,num_heart):
        self.num_eyes=2
        self.num_nose=1
        self.num_heart=num_heart
        
    def eat(self):
        print('i can eat')
    def work(self):
        print('i can work')

class Male:
    def __init__(self,name):
        self.name=name
        
    def flirt(self):
        print('i can flirt') 
    def work(self):
        print('i can code')

class Boy(Human,Male):
    def __init__(self,name,num_heart,language):
        Human.__init__(self,num_heart)
        Male. __init__(self,name)
        self.language=language
    def sleep(self):
        print('i can sleep')
    def work(self):
        print('i can test')
    def display(self):
        print(f"hi i am {self.name} and i work on {self.language}")    
            
boy_1=Boy('virat',1,'python')
# boy_1.work()
# Male.work(boy_1)
# boy_1.sleep()
Human.work(boy_1)
print(boy_1.name)
print(boy_1.num_eyes)
print(boy_1.num_heart)
print(boy_1.language)
boy_1.display() 

# MULTI-LEVEL

class Human:
    def __init__(self,num_heart):
        self.eyes=2
        self.nose=1
        self.heart=num_heart
    def eat(self):
        print('i can eat')
    def work(self):
        print('i can work')
class Male(Human):
    def __init__(self, name):
        self.name=name
    def sleep(self):
        print('i can sleep whole day')
    def work(self):
        print('i can talk')
class Boy(Male):
    def __init__(self, name,num_heart):
        Human.__init__(self,num_heart)
        Male.__init__(self,name)
    def work(self):
        #Human.work(self)
        super().work
        print('i can code')
boy_1=Boy('virat',2)
boy_1.sleep()
boy_1.work()
print(boy_1.eyes)

# HIERARCHICAL 
class Human:
    def __init__(self,name,age):
        print('calling init from human class')
        self.age=age
        self.name=name
    def eat(self):
        print('I can eat')
class Male(Human):
    def __init__(self, m_name, m_age,location):
        print('calling from male calss')
        Human.__init__(self,m_name,m_age)
        self.location=location
    def sleep(self):
        print('i can sleep whole day.')
    def showDetails_m(self):
        print(f"i am {self.name} and my age is {self.age} and i live in {self.location} ")    
class Female(Human):
    def work(self):
        print('I can work')
# female_1=Female(25,'virat')
# female_1.eat()
#print(female_1.name)
male_1=Male('virat',26,'kolkata')
print(male_1.location)
print(Male.mro())
male_1.showDetails_m()

# HYBRID

class A:
    def display(self):
        print('display from A class')
class B(A):
    pass
    #  def display(self):
    #      print('display from b class')
class C(A):
    def show(self):
        print('Hi from C class')
    def display(self):
        print('Hi from c class')    
class D(B,C):
    pass
    # def display(self):
    #     super().display()
    #     print('display from d class')
d1=D() 
d1.display()
print(D.mro())                               





                        