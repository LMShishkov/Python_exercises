# Exercise 40: Is it a Leap Year? Most years have 365 days. However, the time required for the Earth to orbit the Sun is
# actually slightly more than that. As a result, an extra day, February 29, is included in some years to correct for
# this difference. Such years are referred to as leap years. The rules for determining whether or not a year is a leap
# year follow:
# - Any year that is divisible by 400 is a leap year
# - Of the remaining years, any year that is divisible by 100 is not a leap year
# - Of the remaining years, any year that is divisible by 4 is a leap year
# - All other years are not leap years
# Write a program that reads a year from the user and displays a message indicating whether or not it is a leap year.

print('Is it a leap year?')
year = int(input('Please state the year which you would like to check: '))
if year % 400 == 0:
    print(f'{year} is a leap year')
elif year % 100 == 0:
    print(f'{year} is not a leap year')
elif year % 4 == 0:
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')


#Exercise 39: Exercise 39: Cell Phone Bill - A particular cell phone plan includes 50 minutes of air time and 50 text
# messages for $15.00 a month. Each additional minute of air time costs $0.25, while additional text messages cost $0.15
# each. All cell phone bills include an additional charge of $0.44 to support 911 call centers, and the entire bill
# (including the 911 charge) is subject to 5 percent sales tax. Write a program that reads the number of minutes and
# text messages used in a month from the user. Display the base charge, additional minutes charge (if any), additional
# text message charge (if any), the 911 fee, tax and total bill amount. Only display the additional minute and text
# message charges if the user incurred costs in these categories. Ensure that all of the charges are displayed using
# 2 decimal places.

print('The cell phone invoicing tool')
minutes = int(input('Please input the number of minutes and messages used for the given month: '))
messages = int(input('Please input the number of minutes and messages used for the given month: '))
print('-'*10)
base_charge = 15
print('Base charge: {0:.2f}$'.format(base_charge))
extra_minutes = 0
extra_messages = 0
if minutes > 50:
    extra_minutes = (minutes - 50) * 0.25
    print('Extra minutes charge: {0:.2f}$'.format(extra_minutes))
if messages > 50:
    extra_messages = (messages - 50) * 0.15
    print('Extra minutes charge: {0:.2f}$'.format(extra_messages))
support_charge = 0.44
print('Additional 911 call centers support charge: {0:.2f}$'.format(support_charge))
sales_tax_percentage = 0.05
sales_tax = (base_charge + support_charge + extra_minutes + extra_messages) * sales_tax_percentage
print('Sales tax 5% charge: {0:.2f}$'.format(sales_tax))
total_charge = base_charge + support_charge + extra_minutes + extra_messages + sales_tax
print('='*10)
print('')
print('Total charge: {0:.2f}$'.format(total_charge))


# Exercise 38: Wavelengths of Visible Light - The wavelength of visible light ranges from 380 to 750 nanometers (nm).
# While the spectrum is continuous, it is often divided into 6 colors as shown in the chart (check notion.so link for
# chart). Write a program that reads a wave length from the user and reports its color. Display an appropriate error
# message if the wavelength entered by the user is outside of the visible spectrum.

print('Wavelength to color transformator')
wave_len = int(input('Please input the wavelength in nanometers: '))
error_message = False
color = ''
if wave_len < 380 or wave_len > 750:
    error = True
    print(f'Wave with length of {wave_len} nm is outside of the visible spectrum')
elif 380 <= wave_len < 450:
    color = 'Violet'
elif 450 <= wave_len < 495:
    color = 'Blue'
elif 495 <= wave_len < 570:
    color = 'Green'
elif 570 <= wave_len < 590:
    color = 'Yellow'
elif 590 <= wave_len < 620:
    color = 'Orange'
elif 620 <= wave_len < 750:
    color = 'Red'

if error_message is False:
    print(f'Wave with length of {wave_len} nm is in the {color} spectrum')


# Exercise 37: Assessing Employees - At a particular company, employees are rated at the end of each year. The rating
# scale begins at 0.0, with higher values indicating better performance and resulting in larger raises. The value
# awarded to an employee is either 0.0, 0.4, or 0.6 or more. Values between 0.0 and 0.4, and between 0.4 and 0.6 are
# never used. The meaning associated with each rating is shown in the following table. The amount of an employee’s raise
# is $2400.00 multiplied by their rating. Write a program that reads a rating from the user and indicates whether the
# performance was unacceptable, acceptable or meritorious. The amount of the employee’s raise should also be reported.
# Your program should display an appropriate error message if an invalid rating is entered.

print('Employee Assessment and Bonus Program')
emp_rating = float(input('Please input the employee rating: '))
emp_raise_usd = 2400
emp_raise = 0
if emp_rating == 0.0:
    print(f'Employee rating of {emp_rating} means unacceptable performance and {emp_raise}$ raise')
elif emp_rating == 0.4:
    emp_raise = emp_rating * emp_raise_usd
    print(f'Employee rating of {emp_rating} means acceptable performance and {emp_raise}$ raise')
elif emp_rating >= 0.6:
    emp_raise = emp_rating * emp_raise_usd
    print(f'Employee rating of {emp_rating} means meritorious performance and {emp_raise}$ raise')
elif 0 < emp_rating < 0.4 or 0.4 < emp_rating < 0.6:
    print(f'{emp_rating} is invalid')


# Exercise 36: Letter Grade to Grade Points - At a particular university, letter grades are mapped to grade points as
# shown in the chart (check notion.so link for table). Write a program that begins by reading a letter grade from the
# user. Then your program should compute and display the equivalent number of grade points. Ensure that your program
# generates an appropriate error message if the user enters an invalid letter grade.

print('Letter Grade to Grade Points')
grade = input('Please input your letter grade: ')
grade_point = 0
a = 4.0
a_minus = 3.7
b_plus = 3.3
b = 3.0
b_minus = 2.7
c_plus = 2.3
c = 2.0
c_minus = 1.7
d_plus = 1.3
d = 1.0
f = 0
invalid = -1
grade = grade.upper()
if grade == 'A' or grade == 'A+':
    grade_point = a
elif grade == 'A-':
    grade_point = a_minus
elif grade == 'B+':
    grade_point = b_plus
elif grade == 'B':
    grade_point = b
elif grade == 'B-':
    grade_point = b_minus
elif grade == 'C+':
    grade_point = c_plus
elif grade == 'C':
    grade_point = c
elif grade == 'C-':
    grade_point = c_minus
elif grade == 'D+':
    grade_point = d_plus
elif grade == 'D':
    grade_point = d
elif grade == 'F':
    grade_point = f
else:
    grade_point = invalid
if grade_point != invalid:
    print(f'{grade} translates to {grade_point} grade points')
else:
    print(f'{grade} is an invalid letter grade')


# Exercise 35: Chinese Zodiac - The Chinese zodiac assigns animals to years in a 12 year cycle. One 12 year cycle is
# shown in the table (check notion.so link for table with dates). The pattern repeats from there, with 2012 being
# another year of the dragon, and 1999 being another year of the hare. Write a program that reads a year from the user
# and displays the animal associated with that year. Your program should work correctly for any year greater than or
# equal to zero, not just the ones listed in the table.

print('Perpetual Chinese Zodiac')
year_of_birth = int(input('Please input the year of birth: '))
zodiac_sign = 'Dragon'
if year_of_birth % 12 == 9:
    zodiac_sign = 'Snake'
elif year_of_birth % 12 == 10:
    zodiac_sign = 'Horse'
elif year_of_birth % 12 == 11:
    zodiac_sign = 'Sheep'
elif year_of_birth % 12 == 0:
    zodiac_sign = 'Monkey'
elif year_of_birth % 12 == 1:
    zodiac_sign = 'Rooster'
elif year_of_birth % 12 == 2:
    zodiac_sign = 'Dog'
elif year_of_birth % 12 == 3:
    zodiac_sign = 'Pig'
elif year_of_birth % 12 == 4:
    zodiac_sign = 'Rat'
elif year_of_birth % 12 == 5:
    zodiac_sign = 'Ox'
elif year_of_birth % 12 == 6:
    zodiac_sign = 'Tiger'
elif year_of_birth % 12 == 7:
    zodiac_sign = 'Hare'
print(f'{year_of_birth} is the year of {zodiac_sign}')


# Exercise 34 Season from Month and Day - The year is divided into four seasons: spring, summer, fall and winter.
# While the exact dates that the seasons change vary a little bit from year to year because of the way that the calendar
# is constructed, we will use the dates in the chart. Create a program that reads a month and day from the user. The
# user will enter the name of the month as a string, followed by the day within the month as an integer. Then your
# program should display the season associated with the date that was entered.

print('What is the season on this date?')
month, day = input('Please input the full month name and day: ').split()
day = int(day)
season = ''
if month == 'January' or month == 'February':
    season = 'winter'
elif month == 'March':
    if day < 20:
        season = 'winter'
    else:
        season = 'spring'
elif month == 'April' or month == 'May':
    season = 'spring'
elif month == 'June':
    if day < 21:
        season = 'spring'
    else:
        season = 'summer'
elif month == 'July' or month == 'August':
    season = 'summer'
elif month == 'September':
    if day < 22:
        season = 'summer'
    else:
        season = 'autumn'
elif month == 'October' or month == 'November':
    season = 'autumn'
elif month == 'December':
    if day < 21:
        season = 'autumn'
    else:
        season = 'winter'
print(f'{month} {day} is in {season}')

# Exercise 33 (alternative solution)

print('What Color is that square on the Chess Board?')
square_coordinates = input('Please enter the Chess Board square coordinates: ')
first_char = square_coordinates[0]
second_char = square_coordinates[1]
int_second_char = int(second_char)
columns_starting_black = ['a', 'c', 'e', 'g']
if first_char in columns_starting_black:
    if int_second_char % 2 == 0:
        print(f'{square_coordinates} is a white square')
    else:
        print(f'{square_coordinates} is a black square ')
else:
    if int_second_char % 2 == 0:
        print(f'{square_coordinates} is a black square')
    else:
        print(f'{square_coordinates} is a white square ')

# Exercise 33: What Color is that Square? - Positions on a chess board are identified by a letter and a number. The
# letter identifies the column, while the number identifies the row, as shown in the picture.  Write a program that
# reads a position from the user. Use an if statement to determine if the column begins with a black square or a white
# square. Then use modular arithmetic to report the color of the square in that row. For example, if the user enters a1
# then your program should report that the square is black. If the user enters d5 then your program should report that
# the square is white. Your program may assume that a valid position will always be entered. It does not need to perform
# any error checking.

print('What Color is that square on the Chess Board?')
square_coordinates = input('Please enter the Chess Board square coordinates: ')
first_char = square_coordinates[0]
second_char = square_coordinates[1]
int_second_char = int(second_char)
if first_char == 'a' or first_char == 'c' or first_char == 'e' or first_char == 'g':
    if int_second_char % 2 == 0:
        print(f'{square_coordinates} is a white square')
    else:
        print(f'{square_coordinates} is a black square ')
else:
    if int_second_char % 2 == 0:
        print(f'{square_coordinates} is a black square')
    else:
        print(f'{square_coordinates} is a white square ')

# Exercise 32: Date to Holiday Name - Canada has three national holidays which fall on the same dates each year. Write a
# program that reads a month and day from the user (check notion.so link for table with dates). If the month and day
# match one of the holidays listed previously then your program should display the holiday’s name. Otherwise your
# program should indicate that the entered month and day do not correspond to a fixed-date holiday.

print('Date to Holiday Name in Canada')
month, day = input('Enter the full month name and day to check for a holiday: ').split()
if month == 'January' and day == '1':
    print(f'{month} {day} is New year’s day')
elif month == 'July' and day == '1':
    print(f'{month} {day} is Canada day day')
elif month == 'December' and day == '25':
    print(f'{month} {day} is Christmas day day')
else:
    print('The entered month and day does not correspond to a fixed-date holiday')

# Exercise 31: Name that Triangle - A triangle can be classified based on the lengths of its sides as equilateral,
# isosceles or scalene. All 3 sides of an equilateral triangle have the same length. An isosceles triangle has two sides
# that are the same length, and a third side that is a different length. If all of the sides have different lengths then
# the triangle is scalene. Write a program that reads the lengths of 3 sides of a triangle from the user. Display a
# message indicating the type of the triangle.

print('Name that Triangle')
side1, side2, side3 = input('Please input the length of the 3 triangle sides in cm: ').split()
if side1 != side2 != side3:
    print('The triangle is scalene')
elif side1 == side2 == side3:
    print('The triangle is equilateral')
else:
    print('The triangle is isosceles')



# Exercise 30: Sound Levels - The following table (check notion.so link) lists the sound level in decibels for several
# common noises. Write a program that reads a sound level in decibels from the user. If the user enters a decibel level
# that matches one of the noises in the table then your program should display a message containing only that noise. If
# the user enters a number of decibels between the noises listed then your program should display a message indicating
# which noises the level is between. Ensure that your program also generates reasonable output for a value smaller than
# the quietest noise in the table, and for a value larger than the loudest noise in the table.

print('Sound Levels Relation')
sound_level = int(input('Please enter the Decibel level (dB): '))
if sound_level > 130:
    print(f'{sound_level}dBs is louder than a Jackhammer')
if sound_level == 130:
    print(f'{sound_level}dBs is as loud as a Jackhammer')
if 130 > sound_level > 106:
    print(f'{sound_level}dBs is between a Jackhammer and a Gas lawnmower')
if sound_level == 106:
    print(f'{sound_level}dBs is as loud as a Gas lawnmower')
if 106 > sound_level > 70:
    print(f'{sound_level}dBs is between a Gas lawnmower and an Alarm clock')
if sound_level == 70:
    print(f'{sound_level}dBs is as loud as an Alarm clock')
if 70 > sound_level > 40:
    print(f'{sound_level}dBs is between an Alarm clock and a Quiet room')
if sound_level == 40:
    print(f'{sound_level}dBs is as loud as a Quiet room')
if 40 > sound_level:
    print(f'{sound_level}dBs is not louder than a Quiet room')


# Exercise 20: Month Name to Number of Days - The length of a month varies from 28 to 31 days. In this exercise you will
# create a program that reads the name of a month from the user as a string. Then your # program should display the
# number of days in that month. Display “28 or 29 days” for February so that leap years are addressed.

print('Month Name to Number of Days')
month_name = input('Please enter the full name of the month: ')
days = 31
short_months = ['April', 'June', 'September', 'November']
if month_name in short_months:
    days = 30
elif month_name == 'February':
    days = '28 or 29 days'
print(f'{month_name} has {days}')


# Exercise 19: Name that Shape - Write a program that determines the name of a shape from its number of sides. Read the
# number of sides from the user and then report the appropriate name as part of a meaningful message. Your program
# should support shapes with anywhere from 3 up to (and including) 10 sides. If a number of sides outside of this range
# is entered then your program should display an appropriate error message.

print('Name that shape')
nsides = int(input('Enter the number of sides: '))
name = ''
if nsides == 3:
    name = 'triangle'
if nsides == 4:
    name = 'quadrilateral'
if nsides == 5:
    name = 'pentagon'
if nsides == 6:
    name = 'hexagon'
if nsides == 7:
    name = 'heptagon'
if nsides == 8:
    name = 'octagon'
if nsides == 9:
    name = 'nonagon'
if nsides == 10:
    name = 'decagon'

if name == '':
    print(f'{nsides} side(s) are not supported by this program')
else:
    print(f'That is a {name}!')


# Exercise 18:  Vowel or Consonant - In this exercise you will create a program that reads a letter of the alphabet from
# the user. If the user enters a, e, i, o or u then your program should display a message indicating that the entered
# letter is a vowel. If the user enters y then your program should display a message indicating that sometimes y is a
# vowel, and sometimes y is a consonant. Otherwise your program should display a message indicating that the letter is a
# consonant.

print('The vowel or consonant checker')
letter = input('Please input a letter to check: ')
vowels = ['a', 'e', 'i', 'o', 'u']
if letter in vowels:
    print(f'"{letter}" is a vowel')
elif letter == 'y':
    print(f'"{letter}" is sometimes vowel and sometimes consonant')
else:
    print(f'"{letter}" is a consonant')


# Exercise 17: Dog Years - It is commonly said that one human year is equivalent to 7 dog years. However this simple
# conversion fails to recognize that dogs reach adulthood in approximately two years. As a result, some people believe
# that it is better to count each of the first two human years as 10.5 dog years, and then count each additional human
# year as 4 dog years.

print('The dog years converter')
dog_age = int(input('Please enter the age of your dog: '))
dog_human_age = 0
if dog_age <= 0:
    print('Enter a positive number')
elif 0 < dog_age <= 2:
    dog_human_age = dog_age * 10.5
    print(f'Your dog is {dog_human_age}-year old in human years')
elif dog_age > 2:
    dog_human_age = 21 + ((dog_age-2)*4)
    print(f'Your dog is {dog_human_age}-year old in human years')


# Exercise 16: Even or Odd? - Write a program that reads an integer from the user. Then your program should display a
# message indicating whether the integer is even or odd.

print('Number is even - True or False?')
num = int(input('Please input a number: '))
num_even = False
if num % 2 == 0:
    num_even = True
print(num_even)


# Exercise 15: Day Old Bread - A bakery sells loaves of bread for $3.49 each. Day old bread is discounted by 60 percent.
# Write a program that begins by reading the number of loaves of day old bread being purchased from the user. Then your
# program should display the regular price for the bread, the discount because it is a day old, and the total price.
# All of the values should be displayed using two decimal places, and the decimal points in all of the numbers should
# be aligned when reasonable values are entered by the user.

print('The day-old bread discount calculator')
old_bread_loaves = int(input('Please input the number of day-old loaves being purchased: '))
price_std = 3.49
discount_rate = 0.6
price_disc = price_std * discount_rate
total_std = old_bread_loaves * price_std
total_disc = old_bread_loaves * price_disc
discount = total_std - total_disc
print(f'Total regular price for {old_bread_loaves} bread: ', '{0:50.2f}'.format(total_std), '$')
print(f'Total discount for {old_bread_loaves} bread: ', '     {0:50.2f}'.format(discount), '$')
print(f'Total total price for {old_bread_loaves} bread: ', '  {0:50.2f}'.format(total_disc), '$')


# Exercise 14: Sort 3 Integers - Create a program that reads three integers from the user and displays them in sorted
# order (from smallest to largest). Use the min and max functions to find the smallest and largest values. The middle
# value can be found by computing the sum of all three values, and then subtracting the minimum value and the maximum
# value.

print('The 3 integers sorter')
a, b, c = map(int, input('Input 3 random integers: ').split())
biggest = max(a, b, c)
smallest = min(a, b, c)
middle = a + b + c - biggest - smallest
print(smallest, middle, biggest)


# Exercise 13: Area and Volume - Write a program that begins by reading a radius, r , from the user. The program will
# continue by computing and displaying the area of a circle with radius r and the volume of a sphere with radius r .
# Use the pi constant in the math module in your calculations. Hint: The area of a circle is computed using the
# formula area = πr^2. The volume of a sphere is computed using the formula volume = 4/3*πr^3

import math
print('The circle area and sphere volume calculator')
radius = int(input('Please input the radius in centimeters: '))
circle_area = math.pi * (radius ** 2)
sphere_volume = 4 * (math.pi * (radius ** 3)) / 3
print(f'The circle area with radius {radius} is:', ' {0:.2f}'.format(circle_area), ' square centimeters')
print(f'The sphere volume with radius {radius} is:', ' {0:.2f}'.format(sphere_volume), 'cubic centimeters')


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
