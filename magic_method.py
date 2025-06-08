# list1=[1,0,-1]
# print(len(list1))
# print(list1)
# print(type(list1))

class Author:
    def __init__(self,name,book_name,pages):
        self.name=name
        self.book_name=book_name
        self.pages=pages
    def __len__(self):
        return self.pages
    def __call__(self,*args,**kwargs):
        print("hi")
    def __str__(self):
        return f"{self.book_name} by {self.name}"   
d=Author("jenny","python basic to advance",300)
print(d)
print(len(d))
d()        