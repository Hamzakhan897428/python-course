class MyClass:
    a=10
    b=20
p1=MyClass()
print(p1.a)
print(p1.b)

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=Person('jon',23)
print(p1.name)
print(p1.age)
#new changes


#comit from vscode



# class Sum:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return f"{self.name}({self.age})"
# p1=sum('hamza',23)
# print(p1)

class MyPerson:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def fun(self):
        print("hello my is "+self.name)
        print(self.age)
p1=MyPerson('hamza',23)
p1.fun()