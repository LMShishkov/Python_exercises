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


# EX. 2Using the above class createa a separate class and make all instances of the first class also instances of the
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