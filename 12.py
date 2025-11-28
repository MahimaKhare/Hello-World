# Class Object
class car:
    car = " "   
obj1 = car() 
obj1.car = "Audi"
print(obj1.car)  

obj2 = car()
obj2.car = "BMW" 
print(obj2.car)

# Function inside Class
class person:
 def __init__(self,name,age):
    self.name = name
    self.age = age

 def printd(self):
    print(self.name , self.age)
    

user1 = person("Ravi", 23)
user2 = person("sami",21)

user1.printd()
user2.printd()
