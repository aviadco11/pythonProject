#  Class with In Inherince

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I amd {self.age} years old")

    def speak(self):
        print("I don't know what to say")

# here I declare that Pet is father of Cat
class Cat(Pet):
    def speak(self):
        print("Meow")

class Dog(Pet):
    def speak(self):
        print("Bark")

class Fish(Pet):
    pass


# create instance
p = Pet("yosi", 12)
# use speak() method of the father Pet Class
p.speak()

# here it's inherice from Pet class, Child class
c = Cat("Bill", 34)
# use speak() method of the son Cat, override speak father class Pet
c.speak()

d = Dog("ddd", 124)
# use speak() method of the son Dog, override speak father class Pet
d.speak()


# don't have any methods to override, so it will fully inherince from Pet class
f = Fish("ffissh", 22)
f.show()