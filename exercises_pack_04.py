# Exercise 6: Exercise 6: Sum of the First n Positive Integers - Write a program that reads a positive integer, n,
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
