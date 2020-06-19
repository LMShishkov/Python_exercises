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