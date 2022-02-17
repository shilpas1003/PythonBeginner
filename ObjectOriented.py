class Car:
    def __init__(self,name = "XXX",color = "XXX",age = "XXX"):
        self.name = name
        self.color = color
        self.age = age

    def describe(self):
        print("Car name =",self.name)
        print("Car color = ",self.color)
        print("Car age =",self.age)

    def isBanned(self):
        if self.age > 15:
            return True
        else:
            return False

c1 = Car()
c2 = Car("Skoda","black",15)
c1.name = "Mercedes"
c1.color = "Silver"
c1.age = 2
c1.describe()
print(c1.isBanned())
print("different object")
c2.describe()
c2.isBanned()
