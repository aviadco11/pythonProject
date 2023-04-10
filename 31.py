#  Class with In Inherince - more complex.. add extra field to son class (derived class)

# Pet - parent class
# Cat, Dog , Fish = child class

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I amd {self.age} years old")

    def speak(self):
        print("I don't know what to say")

# here I declare Cat with init, because I add extra field color, so it will inherite name and age from Pet class and add color
class Cat(Pet):
    def __init__(self, name, age, color):
        # this inherice from pet name and age, super class is Pet
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I amd {self.age} years old and have color {self.color}")

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
c = Cat("Bill", 34, "Red")
# use speak() method of the child Cat, override speak father class Pet
c.speak()
c.show()

