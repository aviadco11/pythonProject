# class - work class method

class Person:
    number_of_people = 0
    # define constant
    GRAVITY = -9.9

    def __init__(self, name):
        self.name = name
        # this will add t total number of persons in class
        Person.set_person()

    # this mean that the method in class level and not instance level. cls mean class.
    # act on the class himself
    @classmethod
    def number_of_people(cls):
        return cls.number_of_people()

    @classmethod
    def set_person(cls):
        cls.number_of_people = 2


p1 = Person("tim")
p2 = Person("jill")

print(Person.number_of_people)

