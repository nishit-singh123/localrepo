#conditional expression
a=int(input("enter your age:"))
#if elif else ladder
if (a%2==0):
    print("a is even")
# #End of if statement no.1    
if(a>=18):
    print("you are above the age of concent")
    print("good for you")
elif(a<0):
    print("you are entering an invalid age ")
elif(a==0):
    print("you are entering 0 which is invalid age")    
else:
    print("you are below the age of concent")
#end of statement no.2    
print("end of program")
#practice set
#write a program to find the greatest of four numbers entered by user.
a1=int(input("enter number 1:"))
a2=int(input("enter number 2:"))
a3=int(input("enter number 3:"))
a4=int(input("enter number 4:"))
if(a1>a2 and a1>a3 and a1>a4):
    print("greatest number is a1:",a1)
elif(a2>a1 and a2>a3 and a2>a4):
    print("greatest number is a2:",a2)
elif(a3>a1 and a3>a2 and a3>a4):
    print("greatest number is a3 ",a3)
elif(a4>a1 and a4>a2 and a4>a3):
    print("greatest number is a4",a4)
# write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass.assume 3 subjects and take marks as an input from user.        
marks1=int(input("enter marks 1:"))
marks2=int(input("enter marks 2:"))
marks3=int(input("enter marks 3:"))
#check for total percentage 
total_percentage=(100*(marks1+marks2+marks3)/300)
if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("you are pass:",total_percentage)
else:
    print("you are fail , please try next year:",total_percentage)    
#spam comment is defined as a text containing following keywords:"make a lot of money","buy now","subscribe this","click this".write a program to detect these spams.
p1="make a lot of money"
p2="buy now"
p3="subscribe this"
p4="click this"
message=input("enter your comment:")
if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("this comment is a spam")
else:
    print("this is not spam")
# write a program to find whether a given username contains less than 10 characters or not.       
username=input("enter username:")
if (len(username)<10):
    print("username contains less than 10 characters")
else:
    print("all is well")
#write a program to find out whether given name is present in a list or not.
l=["harrry","sonu","monu","rohan"]
name=input("enter your name:")
if (name in l):
    print("your name is in list")
else:
    print("your name is not in the list")    
#write a program to calculate the grade of a student from his marks fro the following scheme:
marks=int(input("enter your marks:"))
if(marks<=100 and marks>=90):
    grade="Excellent"
elif(marks<90 and marks>=80):
    grade="A"
elif(marks<80 and marks>=70):
    grade="B"
elif(marks<70 and marks>=60):
    grade="c"
elif(marks<60 and marks>=50):
    grade="d"
elif(marks<50):
    grade="f"
print("your grade is:",grade) 
#write a program to find out whether a given post is talking about"harry" or not.
post=input("enter the post:")
if("harry"in post.lower):
    print("this post is talking about harry")
else:
    print("this post is talking about harry")        


