# 对象,类及从属关系

# Animal is-a object (yes, sort of confusing ) look at the extra credit


class Animal(object):
    pass

# Animal is a object

# dog is a object
# Animal has a call Dog's instance


class Dog(Animal):
    # dog has a call _init_ object
    def __init__(self, name):
        # ??
        self.name = name


# as top
class Cat(Animal):
    def __init__(self, name):
        # ??
        self.name = name


# is a
class Person(object):
    def __init__(self, name):
        # ??
        self.name = name
        # person has-a pet of some kind
        self.pet = None

# is a

# is a


class Employee(Person):
    def _init_(self, name, salary):
        # ?? hmm what is thie strange magic?
        super(Employee, self).__init__(name)
        # has a
        self.salary = salary


class Fish(object):
    pass


class Halibut(Fish):
    pass

# is a


class Salmon (Fish):
    pass

# ??


# rover is a Dog
rover = Dog("Rover")

# has a
satan = Cat("satan")

# has a
mary = Person("mary")

# has a
mary.pet = satan

# has a
frank = Employee("Frank", 12000)

# has a
frank.pet = rover

#  is a
flipper = Fish()

# is a
crouse = Salmon()

# is a
harry = Halibut()
