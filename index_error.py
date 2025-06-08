def names(salute,*name):
  name=["jenny","payal","jiya","nishit","chandan","shivam","rohit","aziz"]
  length=len(name)
  print(salute)
  
  print(type(name))
  print(name[length-1])
  print()
  print(f"Hi,{name[2]}")
  print(f"Hi,{names[3]}") #index error
  print(f"Hi,{names[length]}") #index error
  print(f"Hi,{name[length-1]}") # it is because length is not equal to last index but last index = length-1.
  print(f"Hi,{name[-7]}")
name2=input('enter your name:')
name1=[]
name1=name2
names('good morning',"jenny","payal","jiya","nishit","chandan","shivam","rohit","aziz")
for i in name1:
  


  names('good morning',name1)