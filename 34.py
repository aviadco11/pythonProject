# statis method, method that not change anything and not access to anything
# it's instead to use method globally, it more organize

class Math:

    @staticmethod
    def add5(x):
        return x + 5

# we don't need to define instance, we can use it like that.
print(Math.add5(5))