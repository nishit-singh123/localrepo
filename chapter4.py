#dictionary&sets
D={}#EMPTY DICTIONARY
marks={
    "harry":100,"shubham":56,"rohan":23
}
print(marks,type(marks))
#METHOD
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"harry":99,"renuka":100})
print(marks)
print(marks.get("harry2"))#prints none
print(marks["harry2"])#returns an error
#SETS
s={1,3,3,4,7,46,7,9,46}#set will take only one element as output 
e=set()#do not use s={}as it will create an emty dictionary
print(s)
#METHODS
s.add(455)
print(s,type(s))
#sets operations
s.remove(1)
s1={1,45,6}
s2={2,6,7,9}
print(s1.union(s2))
print(s1.intersection(s2))
#practice set
#write a program to create a dictionary of hindi words with values as their english translation. provide user with an option to look it up.
words={
    "madad":"help",
    "kursi":"chair",
    "billi":"cat"
}
word=input("enter the word you want meaning of :")
print(words[word])
#write a program to input eight numbers from the user and display all the unique numbers(once).
s=set ()
n=input("enter number:")
s.add(int(n))
n=input("enter number:")
s.add(int(n))
n=input("enter number:")
s.add(int(n))
n=input("enter number:")
s.add(int(n))
n=input("enter number:")
s.add(int(n))
n=input("enter number:")
s.add(int(n))
n=input("enter number:")
s.add(int(n))
print(s)
#can we have a set with 18(int)and '18'(str)as a value in it?
s=set()
s.add(18)
s.add("18")
print(s)
#what will be the length of set:
s=set()
s.add(20)
s.add(20.0)
s.add('20')
print(len(s))
#what is the typeof:
s={}
print(type(s))
#create an empty dictionary.Allow 4 friends to enter their language as value and use key as their names. assume that the names are unique.
d={}
name=input("enter friends name: ")
lang=input("enter language name:")
d.update({name:lang})

name=input("enter friends name: ")
lang=input("enter language name:")
d.update({name:lang})

name=input("enter friends name: ")
lang=input("enter language name:")
d.update({name:lang})

name=input("enter friends name: ")
lang=input("enter language name:")
d.update({name:lang})
print(d)
#if the names of 2 friends are same;what will happen to the program in problem 6?-it will work by update method
#if the language of two friends are same;what will happen to the program in problem 6?-i think it will not affect
#can you change the values inside a list which is contained in set S?
# s={8,7,12,"harry",[1,2]}-no  

