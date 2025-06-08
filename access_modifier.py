#public specifier
class Student: 
    def __init__(self,name,rollno,age):
        self.name=name #public instance variable
        self._rollno=rollno #protected instance variable
        self.__age=age
    def get_age(self): # encapsulation
        return self.__age
    def set_age(self,age):
        if age>35:
            print("invalid age given,, age should be less than 35")
        else:
            self.__age=age        
    def __display(self):
        print(f"hi myself {self.name} {self.__age} years old with rollno {self._rollno} from Student class")
    def displayPrivateData(self):
        self.__display()
class Branch(Student):
    pass
def showData():
    b1=Branch('Nishit',1)
    print(b1.name)
    print(b1._rollno)
    b1.display()        
s1=Student('Rahul',45,60)
b1=Branch("nishit",22)
s1.name='Raunak' #modified
s1._rollno=45
print(s1.name)
print(s1._rollno)
print(s1._Student__age)
s1._Student__display()
print(s1.__age)
s1.displayPrivateData()
showData()
print(s1.get_age())
s1.set_age(34)
print(s1.get_age())




