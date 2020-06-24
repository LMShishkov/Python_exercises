# EX. 1 Calculate down payment of a house which costs $1m, based on the credit rating. Utilizes - basic application of
# built-in input() function along with if condition based on user input options:

price = 1000000
credit_rating = input('Is your credit rating good? True or False?: ')
if credit_rating == 'True':
    down_payment = price*0.15
if credit_rating == 'False':
    down_payment = price*0.275
print(f"Down payment: ${down_payment}")


# EX. 2 Ask for user input and return a message based on the input. Utilizes - basic application of built-in input()
# function along with if condition based on length:

name = input("Type your name: ")
if len(name) < 3:
    print('Name must be at least 3 characters!')
elif len(name) > 50:
    print('Name can be a maximum of 50 characters!')
else:
    print('Name looks good!')


# EX. 3 Simple converter with two options stored in if/else statement:

weight = input("Weight: ")
weight_type = input ("(L)bs or (K)kg: ")
if weight_type == 'K':
    print(int(weight) * 2.20)
else:
    print(int(weight) * 0.453592)


# EX. 4 Simple converter with more checks and two while loops

dist_sys = ''
dist = float()
while dist <= 0:
    dist = float(input('Enter distance> '))
    if dist <=0:
        print('Enter number bigger than 0')
else:
    while dist_sys != 'Km' and 'Mi':
        dist_sys = input('Enter Km or Mi> ')
        if dist_sys == 'Km':
            dist = dist * 0.6214
            print(f'{dist} miles')
        elif dist_sys == "Mi":
            dist = dist * 1.60934
            print(f'{dist} kilometers')
        else:
            print('Invalid distance measure')


# EX. 5 Guess the number game - version 1 (random-generated number):

import random
guesses_made = 0
name = input('Hello! What is your name?\n')
number = random.randint(1, 20)
print ('Well, {0}, I am thinking of a number between 1 and 20.'.format(name))
while guesses_made < 6:
    guess = int(input('Take a guess: '))
    guesses_made += 1
    if guess < number:
        print ('Your guess is too low.')
    if guess > number:
        print ('Your guess is too high.')
    if guess == number:
        break
if guess == number:
    print ('Good job, {0}! You guessed my number in {1} guesses!'.format(name, guesses_made))
else:
    print ('Nope. The number I was thinking of was {0}'.format(number))


# EX. 6 Guess the number game - version 2 (non-random generated number):

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_limit > guess_count:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
else:
    print("Sorry you failed!")


# EX. 7 Guess the number game - version 3 (random-generated number):

import random
number = random.randint(1, 20)
guess_made = 0
while guess_made < 6:
    guess = int(input("Guess: "))
    guess_made += 1
    if guess < number:
        print ("Your number is too low")
    if guess > number:
        print ("Your number is too high")
    if guess == number:
        print("You won! You guessed my number in {0} guesses!".format(guess_made))
        break
else:
    print("Sorry you failed! The number I was thinking was {0}".format(number))


# EX. 8 Car game with comands, feedback, help menu and quit option

command = ""
started = False
help = '''start - to start the car
stop - to stop the car
quit - to exit'''
while command != "quit":
    command = input("> ").lower()
    if command == "help":
        print(help)
    elif command == "start":
        if started:
            print("The car has already started")
        else:
            started = True
            print("Car stared...Ready to go!")
    elif command == "stop":
        if not started:
            print("The car has already stopped")
        else:
            started = False
            print("Car stopped.")
    elif command != "quit":
        print("I don't understand that...")


# EX. 9 Emoji Converter as a function and example on how to call it back

def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)": "😀",
        ":(": "😕"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(f'> ')
print(emoji_converter(message))


# EX. 10 Age input with exceptions for strings and 0 which does not exit until age input is not > 0

age = 0
while age == 0:
    try:
        age = int(input('Age: '))
        zero_check = 1 / age
        print(age)
    except ZeroDivisionError:
        print('Age cannot be 0, try again')
    except ValueError:
        print('Invalid value, try again')


# EX. 11 Factorial calculator with checks for negative and 0 + loop for non-numeric inputs

number =''
while not number.isnumeric():
    number = input('Please input the number:')
    if number.isnumeric():
        num = int(number)
        if num == 0:
            print('0! factorial is 1')
        else:
            fact = 1
            for i in range(1, num + 1):
                fact = fact * i
            print(number + '! factorial is', str(fact))
    else:
        print('Not an integer number')


# EX. 12 Complex calculator with menu and separate reusable functions

def add(x, y):
    """" Adds two numbers """
    return x + y


def subtract(x, y):
    """ Subtracts two numbers """
    return x - y


def multiply(x, y):
    """ Multiples two numbers """
    return x*y


def divide(x, y):
    """Divides two numbers"""
    return x / y


def check_if_user_has_finished():
    """
    Checks that the user wants to finish or not.
    Performs some verification of the input."""
    ok_to_finish = True
    user_input_accepted = False
    while not user_input_accepted:
        user_input = input('Do you want to finish (y/n): ')
        if user_input == 'y':
            user_input_accepted = True
        elif user_input == 'n':
            ok_to_finish = False
            user_input_accepted = True
        else:
            print('Response must be (y/n), please try again')
    return ok_to_finish


def get_operation_choice():
    input_ok = False
    while not input_ok:
        print('Menu Options are:')
        print('\t1. Add')
        print('\t2. Subtract')
        print('\t3. Multiply')
        print('\t4. Divide')
        print('-----------------')
        user_selection = input('Please make a selection: ')
        if user_selection in ('1', '2', '3', '4'):
            input_ok = True
        else:
            print('Invalid Input (must be 1 - 4)')
            print('-----------------')
    return user_selection


def get_numbers_from_user():
    num1 = get_integer_input('Input the first number: ')
    num2 = get_integer_input('Input the second number: ')
    return num1, num2


def get_integer_input(message):
    value_as_string = input(message)
    while not value_as_string.isnumeric():
        print('The input must be an integer')
        value_as_string = input(message)
    return int(value_as_string)

finished = False
while not finished:
    result = 0
    menu_choice = get_operation_choice()
    n1, n2 = get_numbers_from_user()
    if menu_choice == '1':
        result = add(n1, n2)
    elif menu_choice == '2':
        result = subtract(n1, n2)
    elif menu_choice == '3':
        result = multiply(n1, n2)
    elif menu_choice == '4':
        result = divide(n1, n2)
    print('Result:', result)
    print('=================')
    finished = check_if_user_has_finished()

print('Bye')


# EX. 13 Complex calculator (above) + power and modulo options

def add(x, y):
    """" Adds two numbers """
    return x + y


def subtract(x, y):
    """ Subtracts two numbers """
    return x - y


def multiply(x, y):
    """ Multiples two numbers """
    return x * y


def divide(x, y):
    """Divides two numbers"""
    return x / y

def divide2(x, y):
    """Divides two integer numbers"""
    return  x // y

def modulus(x, y):
    """Calculates the modulus between two numbers"""
    return x % y


def power(x, y):
    """Calculates the power between two numbers"""
    return x ** y


def check_if_user_has_finished():
    """
    Checks that the user wants to finish or not.
    Performs some verification of the input."""
    ok_to_finish = True
    user_input_accepted = False
    while not user_input_accepted:
        user_input = input('Do you want to finish (y/n): ')
        if user_input == 'y':
            user_input_accepted = True
        elif user_input == 'n':
            ok_to_finish = False
            user_input_accepted = True
        else:
            print('Response must be (y/n), please try again')
    return ok_to_finish

def get_operation_choice():
    input_ok = False
    while not input_ok:
        print('Menu Options are:')
        print('\t1. Add')
        print('\t2. Subtract')
        print('\t3. Multiply')
        print('\t4. Divide')
        print('\t5. Modulo')
        print('\t6. Power')
        print('-----------------')
        user_selection = input('Please make a selection: ')
        if user_selection in ('1', '2', '3', '4', '5', '6'):
            input_ok = True
        else:
            print('Invalid Input (must be 1 - 6)')
            print('-----------------')
    return user_selection


def get_numbers_from_user():
    num1 = get_integer_input('Input the first number: ')
    num2 = get_integer_input('Input the second number: ')
    return num1, num2


def get_integer_input(message):
    value_as_string = input(message)
    while not value_as_string.isnumeric():
        print('The input must be an integer or float')
        value_as_string = input(message)
    return int(value_as_string)

finished = False
while not finished:
    result = 0
    menu_choice = get_operation_choice()
    n1, n2 = get_numbers_from_user()
    if menu_choice == '1':
        result = add(n1, n2)
    elif menu_choice == '2':
        result = subtract(n1, n2)
    elif menu_choice == '3':
        result = multiply(n1, n2)
    elif menu_choice == '4':
        result = divide(n1, n2)
    elif menu_choice == '5':
        result = modulus(n1, n2)
    elif menu_choice == '6':
        result = power(n1, n2)
    print('Result:', result)
    print('=================')
    finished = check_if_user_has_finished()

print('Bye')

# EX. 14 Program that determines if a given number is a Prime Number or not

def is_prime(n, i=2):
    # Base cases
    if n <= 2:
        return True if (n == 2) else False
    if n % i == 0:
        return False
    if i * i > n:
        return True

    # Check for next divisor
    return is_prime(n, i + 1)


print('is_prime(9):', is_prime(9))


# EX. 15 Currency converter with Curried Function

def convert(x, y):
    return x * y


def curry(funct, num):
    return lambda y: funct(num, y)


dollars_to_sterling = curry(convert, 0.77)
print(dollars_to_sterling(5))

euro_to_sterling = curry(convert, 0.88)
print(euro_to_sterling(15))

sterling_to_dollars = curry(convert, 1.3)
print(sterling_to_dollars(7))

sterling_to_euro = curry(convert, 1.14)
print(sterling_to_euro(9))

# EX. 16 Create object of dogs and write a function which determines which is the oldest accessing their age argments -
# two options (1) with a for loop and (2) with a max function

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


rex = Dog('Rex', 2)
rocky = Dog('Rocky', 45)
mark = Dog('Mark', 14)

def get_biggest_number(*dogs):
    oldest_dog = 0
    for dog in dogs:
        if oldest_dog < dog:
            oldest_dog = dog
    return f'The oldest dog is {oldest_dog} years old'

print(get_biggest_number(rex.age, rocky.age, mark.age))

# alternative solution

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


rex = Dog('Rex', 2)
rocky = Dog('Rocky', 45)
mark = Dog('Mark', 14)

def get_biggest_number(*args):
    return max(args)


print("The oldest dog is {} years old.".format(get_biggest_number(rex.age, rocky.age, mark.age)))