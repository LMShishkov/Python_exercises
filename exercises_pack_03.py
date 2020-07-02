# EX. 1 Create class with formal attributes, class attributes, method and a separate function to calculcate which of
# the class instances has the highest integer value for the age parameter. Create the oldest dog function without
# using the built-in one:

def get_oldest_dog(dogs):
    oldest_dog = 0
    oldest_dog_name = ''
    for dog in dogs:
        if oldest_dog < dog.age:
            oldest_dog = dog.age
            oldest_dog_name = dog.name
    return f'The oldest dog is {oldest_dog_name}, {oldest_dog_name} is {oldest_dog}'


class Dog:

    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return self.name, self.age

    def speak(self, sound):
        return "%s says %s" % (self.name, sound)


d1 = Dog('Pinkie', 3)
d2 = Dog('Charlie', 4)
d3 = Dog('Ben', 5)
dogs = [d1, d2, d3]

print(get_oldest_dog(dogs))


# EX. 2 Using the above class create a a separate class and make all instances of the first class also instances of the
# second class. Also adopt class inheritance for the first class and instantiate objects from the sub-classes.
# Without using a classmethod count the number of instances and display it.

class Pets:

    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs


class Dog:

    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return self.name, self.age

    def speak(self, sound):
        return "%s says %s" % (self.name, sound)

class RussellTerrier(Dog):
    def run(self, speed):
        return "%s runs %s" % (self.name, speed)


class Bulldog(Dog):
    def run(self, speed):
        return "%s runs %s" % (self.name, speed)


my_dogs = [
    Bulldog("Tom", 6),
    RussellTerrier("Fletcher", 7),
    Dog("Larry", 9)
]

my_pets = Pets(my_dogs)


print("I have {} dogs.".format(len(my_pets.dogs)))
for dog in my_pets.dogs:
    print("{} is {}.".format(dog.name, dog.age))

print("And they're all {}s, of course.".format(dog.species))


# EX. 3 Initialize a boolean class variable which is going to define if the dogs are hungry or not for each separate
# object. Create a class method in the main class which going to be used to feed the dogs by simply shifting the same
# class variable to false. Also create a check for the class variable which will print a message to show whether the
# dogs are hungry or not.

class Pets:

    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs


class Dog:

    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True

    def description(self):
        return self.name, self.age

    def speak(self, sound):
        return "%s says %s" % (self.name, sound)

    def eat(self):
        self.is_hungry = False


class RussellTerrier(Dog):
    def run(self, speed):
        return "%s runs %s" % (self.name, speed)


class Bulldog(Dog):
    def run(self, speed):
        return "%s runs %s" % (self.name, speed)


my_dogs = [
    Bulldog("Tom", 6),
    RussellTerrier("Fletcher", 7),
    Dog("Larry", 9)
]

my_pets = Pets(my_dogs)

# feeding the dogs
for dog in my_pets.dogs:
    dog.eat()

# checking if the dogs are fed
are_my_dogs_hungry = False
for dog in my_pets.dogs:
    if dog.is_hungry:
        are_my_dogs_hungry = True

# printing the result from the check
if are_my_dogs_hungry:
    print("My dogs are hungry.")
else:
    print("My dogs are not hungry.")