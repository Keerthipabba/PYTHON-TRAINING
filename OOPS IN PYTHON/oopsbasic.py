class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age


    def description(self):
        print(f"Hi my name is {self.name} and she/he is {self.age}")

class Dog(Animal):
    def __init__(self,name,age,breed):
        super().__init__(name, age)
        self.breed=breed

class Parrot(Animal):
    def __init__(self,name,age,breed):
        super().__init__(name,age)
        self.breed=breed

    def description(self):
        print(f"this is {self.name} is cute and he is {self.age} old. His breed is {self.breed}")

dog=Dog("yuvraj",age=5,breed="pomerian")
animal=Animal(name="leo",age=3)
Parrot=Parrot(name="rakshi",age=1,breed="yellow")

dog.description()
Parrot.description()