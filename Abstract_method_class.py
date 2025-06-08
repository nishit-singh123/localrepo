from  abstract_method_class2 import Vehicle  
class Bike(Vehicle):
    def __init__(self,color,n):
        super().__init__(n)
        self.no_of_tyres=2
        self.color=color
    def start(self):
        print('start with kick')
class Scooty(Vehicle):
    def __init__(self):
        super().__init__()
        
        self.no_of_tyres=2
    def start(self):
        print('self start')
class Car(Vehicle):
    def __init__(self,n):
        super().__init__(n)
        
        self.no_of_gears=6
        self.no_of_tyres=4
    def start (self):
        print("start with key")            