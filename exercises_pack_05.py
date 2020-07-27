# Exercise 8: Write a separate Privileges class. The class should have one attribute, privileges, that stores a list
# of strings as described in Exercise 7. Move the show_privileges() method to this class. Make a Privileges instance
# as an attribute in the Admin class. Create a new instance of Admin and use your method to show its privileges.

privileges_default = ['can add post', 'can delete post', 'can ban user']


class Privileges():

    def __init__(self, privileges=None):
        if privileges is None:
            privileges = privileges_default
        self.privileges = privileges

    def show_privileges(self):
        print(f'Privileges for Admin User are: {self.privileges}')


class User():
    class_id = 0

    @classmethod
    def class_id_update(cls):
        cls.class_id += 1

    def __init__(self, first_name, last_name, status):
        User.class_id_update()
        self.first_name = first_name
        self.last_name = last_name
        self.status = status
        self.id = User.class_id
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f'Resetting login for user ID: {self.id}...')

    def describe_user(self):
        print(f'User names:{self.first_name} {self.last_name} | User status: {self.status} | User ID: {self.id} | '
              f'Login Attempts: {self.login_attempts}')

    def greet_user(self):
        print(f'Hello {self.first_name} {self.last_name}!')


class Admin(User):

    def __init__(self, first_name, last_name, status):
        super().__init__(first_name, last_name, status)
        User.class_id_update()
        self.first_name = first_name
        self.last_name = last_name
        self.status = status
        self.id = User.class_id
        self.login_attempts = 0
        self.privileges_list = Privileges()


privileges_default = ['can add post', 'can delete post', 'can ban user']
user4 = Admin('Don', 'King', 'active')
user4.privileges_list.show_privileges()


# Exercise 7: An administrator is a special kind of user. Write a class called Admin that inherits from the User class
# in Exercise 5 Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can
# ban user", and so on. Write a method called show_privileges() that lists the administrator’s set of privileges. Create
# an instance of Admin, and call your method.


class User():
    class_id = 0

    @classmethod
    def class_id_update(cls):
        cls.class_id += 1

    def __init__(self, first_name, last_name, status):
        User.class_id_update()
        self.first_name = first_name
        self.last_name = last_name
        self.status = status
        self.id = User.class_id
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f'Resetting login for user ID: {self.id}...')

    def describe_user(self):
        print(f'User names:{self.first_name} {self.last_name} | User status: {self.status} | User ID: {self.id} | '
              f'Login Attempts: {self.login_attempts}')

    def greet_user(self):
        print(f'Hello {self.first_name} {self.last_name}!')


class Admin(User):

    def __init__(self, first_name, last_name, status, priviledges_list):
        super().__init__(first_name, last_name, status)
        User.class_id_update()
        self.first_name = first_name
        self.last_name = last_name
        self.status = status
        self.id = User.class_id
        self.login_attempts = 0
        self.privileges_list = priviledges_list

    def show_privileges(self):
        print(f'Privileges for Admin User are: {self.privileges_list}')


privileges_default = ['can add post', 'can delete post', 'can ban user']
user4 = Admin('Don', 'King', 'active', privileges_default)
user4.show_privileges()



# Exercise 6: An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that inherits from
# the Restaurant class in Exercise 3. Add an attribute called flavors that stores a list of ice cream flavors. Write a
# method that displays these flavors. Create an instance of IceCreamStand, and call this method.


class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'{self.restaurant_name} has {self.cuisine_type} cuisine | Number of customers served: '
              f'{self.number_served}')

    def open_restaurant(self):
        print(f'{self.restaurant_name} is open!')

    def set_number_served(self, customers):
        self.number_served = customers

    def increment_number_served(self, additional_customers):
        self.number_served += additional_customers


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavor_list):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavor_list

    def get_flavors(self):
        print(f'The flavors offered at {self.restaurant_name} are: {self.flavors}')


flavors = ['Chocolate', 'Mind', 'Vanilla']
restaurant4 = IceCreamStand('Happy Penguin', 'traditional ice-cream', flavors)
restaurant4.describe_restaurant()
restaurant4.get_flavors()


# Exercise 5: Using Exercise 4 as a base - add a class variable called class_id and a class method that creates a new
# class_id for every new object by adding 1 to the previous one recording it in the object itself.

class User():
    class_id = 0

    @classmethod
    def class_id_update(cls):
        cls.class_id += 1

    def __init__(self, first_name, last_name, status):
        User.class_id_update()
        self.first_name = first_name
        self.last_name = last_name
        self.status = status
        self.id = User.class_id
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f'Resetting login for user ID: {self.id}...')

    def describe_user(self):
        print(f'User names:{self.first_name} {self.last_name} | User status: {self.status} | User ID: {self.id} | '
              f'Login Attempts: {self.login_attempts}')

    def greet_user(self):
        print(f'Hello {self.first_name} {self.last_name}!')


user1 = User('John', 'Smith', 'active')
user2 = User('Emma', 'Smith', 'active')
user3 = User('Jena', 'Smith', 'inactive')

user1.describe_user()
user2.describe_user()
user3.describe_user()


# Exercise 4: Using Exercise 2 as a base - add Add an attribute called login_attempts to your User class. Write a
# method called increment_login_attempts() that increments the value of login_attempts by 1. Write another method
# called reset_login_attempts() that resets the value of login_ attempts to 0. Make an instance of the User class and
# call increment_login_attempts() several times. Print the value of login_attempts to make sure it was incremented
# properly, and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.


class User():

    def __init__(self, first_name, last_name, status, id):
        self.first_name = first_name
        self.last_name = last_name
        self.status = status
        self.id = id
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f'Resetting login for user ID: {self.id}...')

    def describe_user(self):
        print(f'User names:{self.first_name} {self.last_name} | User status: {self.status} | User ID: {self.id} | '
              f'Login Attempts: {self.login_attempts}')

    def greet_user(self):
        print(f'Hello {self.first_name} {self.last_name}!')


user1 = User('John', 'Smith', 'active', '123')
user2 = User('Emma', 'Smith', 'active', '456')
user3 = User('Jena', 'Smith', 'inactive', '789')

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.describe_user()
user2.describe_user()
user3.describe_user()

user1.reset_login_attempts()

user1.describe_user()


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
