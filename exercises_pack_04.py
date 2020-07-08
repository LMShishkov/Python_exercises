# Exercise 12: Distance Units - In this exercise, you will create a program that begins by reading a measurement in
# feet from the user. Then your program should display the equivalent distance in inches, yards and miles. Use the
# Internet to look up the necessary conversion factors if you don’t have them memorized.

print('The feet distance converter')
feet = input('Please input the distance in feet: ')
inches_equivalent = int(feet) * 12
yards_equivalent = int(feet) * 0.333
miles_equivalent = int(feet) * 0.000189394
print('The equivalent of ', feet, ' in inches is: {0:.2f}'.format(inches_equivalent))
print('The equivalent of ', feet, ' in yards is: {0:.2f}'.format(yards_equivalent))
print('The equivalent of ', feet, ' in miles is: {0:.2f}'.format(miles_equivalent))


# Exercise 11: Height Units - Many people think about their height in feet and inches, even in some countries that
# primarily use the metric system. Write a program that reads a number of feet from the user, followed by a number of
# inches. Once these values are read, your program should compute and display the equivalent number of centimeters.

print('The height units converter')
feet, inches = input('Please enter your height feet and inches: ').split()
centimeters = (int(feet) * 12 + int(inches)) * 2.54
print(f'Your height is {centimeters} centimeters')


# Exercise 10: Making Change - Consider the software that runs on a self-checkout machine. One task that it must be
# able to perform is to determine how much change to provide when the shopper pays for a purchase with cash. Write a
# program that begins by reading a number of cents from the user as an integer. Then your program should compute and
# display the denominations of the coins that should be used to give that amount of change to the shopper. The change
# should be given using as few coins as possible. Assume that the machine is loaded with pennies, nickels, dimes,
# quarters, loonies and toonies.

print('The change cash-machine converter')
CENTS_PER_TOONIE = 200
CENTS_PER_LOONIE = 100
CENTS_PER_QUARTER = 25
CENTS_PER_DIME = 10
CENTS_PER_NICKEL = 5

change = float(input('Enter the number in $: '))
cents = change*100

print(' ', cents // CENTS_PER_TOONIE, 'toonies')
cents = cents % CENTS_PER_TOONIE

print(' ', cents // CENTS_PER_LOONIE, 'loonies')
cents = cents % CENTS_PER_LOONIE

print(' ', cents // CENTS_PER_QUARTER, 'quarters')
cents = cents % CENTS_PER_QUARTER

print(' ', cents // CENTS_PER_DIME, 'dimes')
cents = cents % CENTS_PER_DIME

print(' ', cents // CENTS_PER_NICKEL, 'nickels')
cents = cents % CENTS_PER_NICKEL

print(' ', cents, 'pennies')


# Exercise 9: Fuel Converter - In the United States, fuel efficiency for vehicles is normally expressed in
# miles-per-gallon (MPG). In Canada, fuel efficiency is normally expressed in liters-per-hundred kilometers (L/100
# km). Use your research skills to determine how to convert from MPGto L/100 km. Then create a program that reads a
# value from the user in American units and displays the equivalent fuel efficiency in Canadian units.

print('The fuel converter')
fuel_consumption_american = int(input('Please input the fuel consumption in miles-per-gallon (MPG): '))
ratio = 235.215
fuel_consumption_canadian = ratio / fuel_consumption_american
print('Fuel consumption in liters-per-100 kilometers (L/100km): {0:.2f}'.format(fuel_consumption_canadian))


# Exercise 8: Compound Interest - Pretend that you have just opened a new savings account that earns 11% interest per
# year. The interest that you earn is paid at the end of the year, and is added to the balance of the savings
# account. Write a program that begins by reading the amount of money deposited into the account from the user. Then
# your program should compute and display the amount in the savings account after 1, 2, and 3 years. Display each
# amount so that it is rounded to 2 decimal places.

print('The bank account interest-rate calculator')
initial_balance = int(input('Please supply your initial balance at the beginning of the period: '))
interst_rate = 0.11
balance_y1_end = initial_balance + initial_balance * interst_rate
balance_y2_end = balance_y1_end + balance_y1_end * interst_rate
balance_y3_end = balance_y2_end + balance_y2_end * interst_rate
print('Balance at the end of Y1 is: {0:.2f}$\nBalance at the end of Y2 is: {1:.2f}$\nBalance at the end of Y3 is: \
{2:.2f}$ \n'.format(balance_y1_end, balance_y2_end, balance_y3_end))


# Exercise 7: Widgets and Gizmos - An online retailer sells two products: widgets and gizmos. Each widget
# weighs 75 grams. Each gizmo weighs 112 grams. Write a program that reads the number of widgets and the number of
# gizmos in an order from the user. Then your program should compute and display the total weight of the order.

print('The widgets and gizmos weight calculator')
widgets, gizmos = input("Enter the amount of widgets and gizmos: ").split()
widget_weight = 75
gizmo_weight = 112
total_weight = int(widgets)*widget_weight + int(gizmos)*gizmo_weight
print(f'The total weight of your order is: {total_weight} grams')


# Exercise 6: Sum of the First n Positive Integers - Write a program that reads a positive integer, n,
# from the user and then displays the sum of all of the integers from 1 to n. The sum of the first n positive
# integers can be computed using the formula: sum = (n)(n + 1)/2

print('Sum of all integers from 1 to n')
n = int(input('Supply a positive integer for n: '))
sum_to_n = (n*(n+1))/2
print(f'Sum of the First {n} Positive Integers is: {sum_to_n}')


# Exercise 5: Tax and Tip - The program that you create for this exercise will begin by reading the cost of a meal
# ordered at a restaurant from the user. Then your program will compute the tax and tip for the meal. Use your local
# tax rate when computing the amount of tax owing. Compute the tip as 18 percent of the meal amount (without the
# tax). The output from your program should include the tax amount, the tip amount, and the grand total for the meal
# including both the tax and the tip. Format the output so that all of the values are displayed using two decimal
# places.

print('This is the Tax & Tip calculator')
tax_rate = 0.2
tip_rate = 0.18
meal_cost = float(input('Please input the cost of your meal: '))
tax = meal_cost * tax_rate
tip = meal_cost * tip_rate
grand_total = meal_cost + tax + tip
print('Tip = {0:.2f}$ \nTax = {1:.2f}$ \nGrand Total = {2:.2f}$'.format(tip, tax, grand_total))


# Exercise 4: Bottle Deposits - In many jurisdictions a small deposit is added to drink containers to encourage
# people to recycle them. In one particular jurisdiction, drink containers holding one liter or less have a $0.10
# deposit, and drink containers holding more than one liter have a $0.25 deposit. Write a program that reads the
# number of containers of each size from the user. Your program should continue by computing and displaying the
# refund that will be received for returning those containers. Format the output so that it includes a dollar sign
# and always displays exactly two decimal places.

print('This is the bottle deposit calculator')
small_container = int(input('Please input the number of small containers to be returned: '))
big_container = int(input('Please input the number of big containers to be returned: '))
refund = small_container * 0.1 + big_container * 0.25
formatted_refund = '{:.2f}'.format(refund)
print(f'Your total refund is {formatted_refund}$')


# Exercise 3: Area of a Field - Create a program that reads the length and width of a farmer’s field from the user in
# feet. Display the area of the field in acres.

print('This is the field area calculator')
field_width = float(input('Please enter the width of your field in feet: '))
field_length = float(input('Please enter the length of your field in feet: '))
field_area = (field_width * field_length) / 43.560
formatted_field_area = '{:.2f}'.format(field_area)
print(f'Your field area is {formatted_field_area} acres')


# Exercise 2: Area of a Room - Write a program that asks the user to
# enter the width and length of a room. Once the values have been read, your program should compute and display the
# area of the room. The length and the width will be entered as floating point numbers. Include units in your prompt
# and output message; either feet or meters, depending on which unit you are more comfortable working with.

print('This is the room area calculator')
room_width = float(input('Please enter the width of your room in meters: '))
room_length = float(input('Please enter the length of your room in meters: '))
room_area = room_width * room_length
print(f'Your room area is {room_area} square meters')


# Exercise 1: Hello - Write a program that asks the user to enter his or her name. The program should respond with a
# message that says hello to the user, using his or her name.

user_name = input('What is your name? ')
print(f'Hello {user_name}!')
