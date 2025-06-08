# def greet():
#     print("Hi jenny,Ram,Raghav")
#     print('Are you from cs department')
# greet()
# def greet(name):# formal parameter
#     print(f"Hi {name}")
# greet("jenny")
# greet("raghav") # argument

# # TYPE OF PARAMETER

# #def greet(name,dept):
# #def greet(name,subject,dept="cs"): # default parameter and it follows positional parameter or non-default   
# def info_person(**numbers):
#     # print(name,age,dept)
#      for key,value in numbers.items():
#          print(key,value)
    
#     #c=0
#     #numbers[0]=4 # it is illigal
#     # for i in numbers:
#     #     c=c+i
#     #     print(f"sum is {c}")
#     # print(numbers)
#     # print(name)    
#     # print(f"Hi {name}")
#     # print(f"Are you from this {dept}  department")
#     # print(f"Do you teach us subject {subject}")
# greet("jenny","cs")# positional argument
# greet(dept="cs",name="jenny")# keyword argument
# greet("jenny",dept='cs')# mixed keyword argument
# greet("jenny","python","IT") # it overrides the default parameter value
# greet('jenny',1,2,3,4,5,6,7,8,9) # arbitrary positinal argument(*args)
# info_person(name="Ram",age=30,dept='cs')


# class BMW:
#     def __init__(self,color,model):
#         self.bmw_color=color
#         self.bmw_model=model
        #self.bmw_origin_palce=origin_place
        #self.bmw_origin_place='GERMANY'
        #print("BMW is the best car")
# BMW_12= BMW('red','3x')
# BMW_12.color="red"
# BMW_12.price="30 lakh"
# BMW_12.model="3x"
#print(BMW_12.bmw_origin_place)

# self init, methods, inheritence
# class homeopathy:
    #performance='slower'
#     def __init__(self,medicine,qaulity,feedback):
#         self.medicine=medicine
#         self.quality=qaulity
#         self.feedback=feedback
#         self.performance="slower" # default to the all the function
        
#     def treat(self,homeo_medicine): # when function is associated with object known as method
#         print(f"hiii this is {self.quality} {homeo_medicine} ")
#     def update_performance(self,performance):
#         self.performance='little faster'
# doctor_1=homeopathy('nasal polybs','better','good')
# doctor_2=homeopathy('heart','good','better')
# doctor_2=homeopathy('asthma','better','best')
# doctor_1.treat('medicine')
# doctor_1.update_performance("little faster")
# print(doctor_1.performance)

# class ClassicalHomeopath(homeopathy):
#    pass   

# doctor_3=ClassicalHomeopath()
# doctor_3.treat('medicine')

# class Human:
#     def __init__(self):
#         self.num_eyes=2
#         self.num_nose=1
#     def eat(self):
#         print('i can eat')
#     def work(self):
#         print('i can work')
# class Male(Human):
#     def __init__(self,name):
#         self.name=name
#     def flirts(self):
#         print('i can flirts')
#     def work(self):
#         super().work()
#         print('i can code')
# male_1=Male('jenny')
# male_1.flirts()
# male_1.work()
# print(male_1.num_eyes) 
# print(male_1.name)

    