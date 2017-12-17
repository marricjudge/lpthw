## Animal is-a object
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is-a animal
class Cat(Animal):

    def __init__(self, name):
        ##Cat has-a name
        self.name = name

class Person(Animal):

    def __init__(self, name):
        ##Person has-a name
        self.name = name
        ##Person has-a pet of some kind
        self.pet = None

## Employee is-a person
class Employee(Person):
    def __init__(self, name, salary):
        ## Employee has a super
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is a Animal
class Fish(object):
    pass

##rover is-a Dog
rover = Dog("Rover")

## Satan is a Cat
satan = Cat("Satan")

##Mary is a person
mary = Person("Mary")

##Mary has a pet called Satan
mary.pet = satan

##Frank is a employee
frank = Employee("Frank", 120000)

##Frank has a pet called rover
frank.pet = rover

##Flipper is a fish
flipper = Fish()

##Crouse is a salmon
crouse = Salmon()

##Hary is a halubut 
harry = Halibut()
