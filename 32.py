# class - work with attribute class

class Person:
    # Define static attribute (class atrribute) for all class, is shards for all instances on the class.
    # use self make the diffrent for every instance in the class
    number_of_people = 0
    # define constant
    GRAVITY = -9.9

    def __init__(self, name):
        self.name = name
        Person.number_of_people += 1

p1 = Person("tim")
p2 = Person("jill")

# can write it with Person,because isn't sepefic for instance
Person.number_of_people = 8
# we see that we get the valus for all
print(p1.number_of_people)
print(p2.number_of_people)
print(Person.number_of_people)
print(Person.number_of_people)
# here we add +1 to number_of_people, then it's increase for every instance creation
p3 = Person("tim")
print(Person.number_of_people)
print(p3.number_of_people)