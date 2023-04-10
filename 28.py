# simple Class

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I amd {self.age} years old")

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set(self, name, age):
        self.name = name
        self.age = age

p = Pet("yosi", 12)
p.show()
print(p.get_name())
print(p.get_age())
p.set("roni", 33)
p.show()