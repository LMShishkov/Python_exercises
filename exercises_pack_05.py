# Exercise 3: Using Exercise 1 as a base - add an attribute called number_served with a default value of 0. Create an
# instance called restaurant from this class. Print the number of customers the restaurant has served, and then change
# this value and print it again. Add a method called set_number_served() that lets you set the number of customers that
# have been served. Call this method with a new number and print the value again. Add a method called
# increment_number_served() that lets you increment the number of customers who’ve been served. Call this method with
# any number you like that could represent how many customers were served in, say, a day of business.


class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'{self.restaurant_name} has {self.cuisine_type} cuisine | Number of customers served so far: '
              f'{self.number_served}')

    def open_restaurant(self):
        print(f'{self.restaurant_name} is open!')

    def set_number_served(self, customers):
        self.number_served = customers
        print(f'Setting the number of customers served to {self.number_served} customers')
        self.describe_restaurant()

    def increment_number_served(self, additional_customers):
        self.number_served += additional_customers
        print(f'Increasing the number of customers served to {self.number_served} customers')
        self.describe_restaurant()


restaurant = Restaurant('Red Dragon', 'Chinese')
restaurant.describe_restaurant()
restaurant.set_number_served(13)
restaurant.increment_number_served(1)


# Exercise 2: Make a class called User. Create two attributes called first_name and last_name, and then create several
# other attributes that are typically stored in a user profile. Make a method called describe_user() that prints a
# summary of the user’s information. Make another method called greet_user() that prints a personalized greeting to the
# user. Create several instances representing different users, and call both methods for each user.


class User():

    def __init__(self, first_name, last_name, status, id):
        self.first_name = first_name
        self.last_name = last_name
        self.status = status
        self.id = id

    def describe_user(self):
        print(f'User names:{self.first_name} {self.last_name} | User status: {self.status} | User ID: {self.id}')

    def greet_user(self):
        print(f'Hello {self.first_name} {self.last_name}!')


user1 = User('John', 'Smith', 'active', '123')
user2 = User('Emma', 'Smith', 'active', '456')
user3 = User('Jena', 'Smith', 'inactive', '789')

user1.greet_user()
user2.greet_user()
user3.greet_user()

user1.describe_user()
user2.describe_user()
user3.describe_user()


# Exercise 1: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a
# restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indicating that the restaurant is open. Make
# an instance called restaurant from your class. Print the two attributes individually, and then call both methods.


class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'{self.restaurant_name} has {self.cuisine_type} cuisine')

    def open_restaurant(self):
        print(f'{self.restaurant_name} is open!')


restaurant = Restaurant('Crippled Goose', 'English')
restaurant.describe_restaurant()
restaurant.open_restaurant()
