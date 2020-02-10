## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a animal
class Dog(Animal):

    def __init__(self, name):
        ## self.name attribute of Dog class has-a name parameter
        self.name = name

#Cat is-a animal
class Cat(Animal):
    def __init__(self, name):
        ## self.name attribute of Cat class has-a name parameter
        self.name = name


## Person is-a object
class Person(object):

        def __init__(self, name):
            ## self.name attribute of Person class has-a name parameter
            self.name = name

            ## Person has-a pet of some kind
            self.pet = None

## Employee is-a person
class Employee(Person):
    def __init__(self, name, salary):
        ## Employee has-a name which it inherits from Person
        super(Employee, self).__init__(name)
        ## self.salary attribute of Employee class has salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a fish
class Salmon(Fish):
    pass

## Halibut is-a fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")

## mary has-a pet satan
mary.pet = satan

## frank is-a Employee and has-a salary of 120000
frank = Employee("Frank", 120000)

## frank has-a pet rover
frank.pet = rover

## flipper is an instance of fish
flipper = Fish()

## crouse is an instance of salmon
crouse = Salmon()

## harry is an instance of Halibut
harry = Halibut()
