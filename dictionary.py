phone_no={'name':1234,
          'shyam':3456,'mohan':6798,
          'name':3456}
print(phone_no)
print(phone_no['shyam'])
phone_number=dict([('name',1234),
          ('shyam',3456),('mohan',6798),
          ('name',3456)])
print(phone_no)
phone_no['shyam']={1234,6788,7865,987,76776}
print(phone_no)
print(phone_no.get('Shyam'))
data={
    1:'jenny',
    2:'ram',
    0:'mohan'
}
print(data[0]) # it  is not index but key value. 
del data[1]
print(data)
print(data.pop(0)) # it wiil return value
print(data.popitem())# it will return kay and value
print(data)

print(data.keys())
print(data.values())
print(data.items()) 
for i in data:
      print(i)
      print (data[i]) 

dict_1=data.copy()
print(dict_1)
print(len(dict_1))

# NESTED

student_data={
      'ram':{'roll_no':10,'age':20,'course':'python'},
      'mohan':{'roll_no':20,"age":22,"course":"java"}

}
print(student_data["mohan"]) # it is a subscript
print(student_data["mohan"]["roll_no"])
student_data['mohan']['phone_number']=987666556565
print(student_data)
print(student_data['mohan'])
student_data['mohan']['phone_number']
print(student_data['mohan'].pop('phone_number'))
print(student_data['mohan'])

# NESTING A LIST WITHIN A DICTIONARY

travel_data={
    'gujrat':['dwarkadish','somnath','statue of unity'],
    'rajasthan':['jaipur','udaipur']
    }
print(travel_data['rajasthan'])

student_data=[
      {'name':'ram',
       'roll_no':10,
       'age':20,
       'course':'python'
       },
      {
          'name':'mohan',
          'roll_no':20,
          "age":22,
          "course":"java",
          'phone_no':[87546567,78]
          }
] 
print(student_data[1]) # ACCESS THROUGH INDEX
print(student_data[1]['phone_no'])

#CODING EXERCISE

student_data=[
      {'name':'ram',
       'roll_no':10,
       'age':20,
       'course':'python'
       },
      {
          'name':'mohan',
          'roll_no':20,
          "age":22,
          "course":"java",
          'phone_no':[87546567,78]
          }
] 
def add_new_student(name,rollno,age,course_opted):
    new_student={}
    new_student['Name']=name
    new_student['roll_no']=rollno
    new_student['age']=age
    new_student['course']=course_opted
    print(student_data.append(new_student))
       
    
add_new_student('shyam',22,18,'c++')
print(student_data)

# CODING EXERCISE

student_marks={
    'jenny':87,
    'harry':78,
    'dimpy':56,
    'rahul':41,
    'aniket':99,
    'prem':34
}
student_grades={}
for i in student_marks:
    marks=student_marks[i]
    if marks>90:
        student_grades[i]='A+'
    elif marks>80:
        student_grades[i]='A'
    elif marks>70:
        student_grades[i]='B++'
    elif marks>60:
        student_grades[i]='B'
    elif marks>50:
        student_grades[i]='c'
    elif marks>40:
        student_grades[i]='d'
print(student_grades)                        

  


    