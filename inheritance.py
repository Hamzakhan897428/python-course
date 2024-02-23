class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()
class person:
  def __init__(self,firstname,lastname):
    self.firstname=firstname
    self.lastname=lastname
  def PrintName(self):
    print(self.firstname,self.lastname)
class Student(person):
  def __init__(self, firstname, lastname,year):
    super().__init__(firstname,lastname)
    self.graduationyear=year
  
  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()






