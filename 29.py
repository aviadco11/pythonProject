#  Class with In Inherince

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I amd {self.age} years old")

# here I declare that Pet is father of Cat
class Cat(Pet):
    def speak(self):
        print("Meow")

class Dog(Pet):
    def speak(self):
        print("Bark")


# create instance
p = Pet("yosi", 12)
p.show()

# here it's inherice from Pet class
c = Cat("Bill", 34)
c.show()

d = Dog("ddd", 124)
d.show()