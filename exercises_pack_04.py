# Exercise 66:  Is it a Valid Triangle? - If you have 3 straws, possibly of differing lengths, it may or may not be
# possible to lay them down so that they form a triangle when their ends are touching. For example, if all of the straws
# have a length of 6 inches. then one can easily construct an equilateral triangle using them. However, if one straw is
# 6 inches. long, while the other two are each only 2 inches. long, then a triangle cannot be formed. In general, if any
# one length is greater than or equal to the sum of the other two then the lengths cannot be used to form a triangle.
# Otherwise they can form a triangle. Write a function that determines whether or not three lengths can form a triangle.
# The function will take 3 parameters and return a Boolean result. In addition, write a program that reads 3 lengths
# from the user and demonstrates the behaviour of this function.

def triangle_check(a, b, c):
    check = True
    if a >= b + c or b >= a + c or c >= a + b:
        check = False
    return check


def main():
    print('Is it a valid triangle?')
    num1, num2, num3 = input('Please input 3 side-lengths to check if they can form a triangle: ').split()
    print('Answer: ', triangle_check(int(num1), int(num2), int(num3)))


# Exercise 65:  The Twelve Days of Christmas - The Twelve Days of Christmas is a repetitive song (lyrics available
# online) that describes an increasingly long list of gifts sent to one’s true love on each of 12 days. A single gift is
# sent on the first day. A new gift is added to the collection on each additional day, and then the complete collection
# is sent. Your task is to write a program that displays the complete lyrics for The Twelve Days of Christmas. Write a
# function that takes the verse number as its only parameter and displays the specified verse of the song. Then call
# that function 12 times with integers that increase from 1 to 12. Each item that is sent to the recipient in the song
# should only appear once in your program, with the possible exception of the partridge. It may appear twice if that
# helps you handle the difference between “A partridge in a pear tree” in the first verse and “And a partridge in a pear
# tree” in the subsequent verses. Import your solution to Exercise 85 to help you complete this exercise.

def xmas_song_lyrics(a):
    verse = ''
    base = 'On the {0} day of Christmas\nmy true love sent to me:'
    end = '\nAnd a partridge in a pear tree.'
    ver1 = '\nA partridge in a pear tree'
    ver2 = '\nTwo turtle doves,' + end
    ver3 = '\nThree French hens,' + ver2
    ver4 = '\nFour calling birds,' + ver3
    ver5 = '\nFive gold rings,' + ver4
    ver6 = '\nSix geese a laying,' + ver5
    ver7 = '\nSeven swans a swimming,' + ver6
    ver8 = '\nEight maids a milking,' + ver7
    ver9 = '\nNine ladies dancing,' + ver8
    ver10 = '\nTen lords a leaping,' + ver9
    ver11 = '\nEleven pipers piping,' + ver10
    ver12 = '\n12 drummers drumming,' + ver11
    if a == 1:
        ord = 'first'
        verse = base.format(ord) + ver1
    elif a == 2:
        ord = 'second'
        verse = base.format(ord) + ver2
    elif a == 3:
        ord = 'third'
        verse = base.format(ord) + ver3
    elif a == 4:
        ord = 'fourth'
        verse = base.format(ord) + ver4
    elif a == 5:
        ord = 'fifth'
        verse = base.format(ord) + ver5
    elif a == 6:
        ord = 'sixth'
        verse = base.format(ord) + ver6
    elif a == 7:
        ord = 'seventh'
        verse = base.format(ord) + ver7
    elif a == 8:
        ord = 'eight'
        verse = base.format(ord) + ver8
    elif a == 9:
        ord = 'ninth'
        verse = base.format(ord) + ver9
    elif a == 10:
        ord = 'tenth'
        verse = base.format(ord) + ver10
    elif a == 11:
        ord = 'eleventh'
        verse = base.format(ord) + ver11
    elif a == 12:
        ord = 'twelfth'
        verse = base.format(ord) + ver12
    return verse + '\n'

def main(b):
    for i in range(1, b+1):
        print(xmas_song_lyrics(i))


# Exercise 64: Convert an Integer to its Ordinal Number - Words like first, second and third are referred to as ordinal
# numbers. In this exercise, you will write a function that takes an integer as its only parameter and returns a string
# containing the appropriate English ordinal number as its only result. Your function must handle the integers between
# 1 and 12 (inclusive). It should return an empty string if a value outside of this range is provided as a parameter.
# Include a main program that demonstrates your function by displaying each integer from 1 to 12 and its ordinal number.

def ord_converter(a):
    if a == 1:
        ord = 'first'
    elif a == 2:
        ord = 'second'
    elif a == 3:
        ord = 'third'
    elif a == 4:
        ord = 'fourth'
    elif a == 5:
        ord = 'fifth'
    elif a == 6:
        ord = 'sixth'
    elif a == 7:
        ord = 'seventh'
    elif a == 8:
        ord = 'eight'
    elif a == 9:
        ord = 'ninth'
    elif a == 10:
        ord = 'tenth'
    elif a == 11:
        ord = 'eleventh'
    elif a == 12:
        ord = 'twelfth'
    else:
        ord = ''
    return ord


def main():
    print('The Ordinal Number converter')
    num = int(input('Please input an integer from 1 - 12: '))
    if num > 12:
        print('The ordinal is not supported!')
    else:
        print('The ordinal for {0} is {1}'.format(num, ord_converter(num)))


# Exercise 63: Median of Three Values - Write a function that takes three numbers as parameters, and returns the
# median value of those parameters as its result. Include a main program that reads three values from the user and
# displays their median.

def median_val(a, b, c):
    return a + b + c - min(a, b, c) - max(a, b, c)


def main():
    print('Median of three values')
    v1, v2, v3 = input('Please input three values to confirm their median: ').split()
    print('The median of {0}, {1} and {2} is {3}'.format(v1, v2, v3, median_val(float(v1), float(v2), float(v3))))


# Exercise 62: Shipping Calculator - An online retailer provides express shipping for many of its items at a rate of
# $10.95 for the first item, and $2.95 for each subsequent item. Write a function that takes the number of items in
# the order as its only parameter. Return the shipping charge for the order as the function’s result. Include a main
# program that reads the number of items purchased from the user and displays the shipping charge.

def shipping_calc(items):
    first_item = 10.95
    next_item = 2.95
    charge = first_item + (items - 1) * next_item
    return charge


def main():
    print('The Shipping Calculator')
    your_items = int(input('Please input the number of items you would like to get the shipping charge for: '))
    print('The shipping charge for {0} item(s) is {1:.2f}$'.format(your_items, shipping_calc(your_items)))


# Exercise 61: Taxi Fare - In a particular jurisdiction, taxi fares consist of a base fare of $4.00, plus $0.25 for
# every 140 meters traveled. Write a function that takes the distance traveled (in kilometers) as its only parameter
# and returns the total fare as its only result. Write a main program that demonstrates the function.

def taxi_fare(dist):
    base_fare = 4
    var_fare = 0.25
    dist_m = dist * 1000
    fare = base_fare + (dist_m/140)*var_fare
    return fare


def main():
    print('Taxi Fare Calculator')
    distance = float(input('Please input the distance traveled in kilometers: '))
    print('The total fare for {0:.2f} kilometers travelled is {1:.2f}$'.format(distance, taxi_fare(distance)))


# Exercise 60: Compute the Hypotenuse - Write a function that takes the lengths of the two shorter sides of a right
# triangle as its parameters. Return the hypotenuse of the triangle, computed using pythagorean theorem,
# as the function’s result. Include a main program that reads the lengths of the shorter sides of a right triangle
# from the user, uses your function to compute the length of the hypotenuse, and displays the result.

import math

def hypotenuse_calc(a, b):
    z = (a*a) + (b*b)
    c = math.sqrt(z)
    return c


def main():
    print('The Hypotenuse Calculator')
    s1, s2 = input('Please input the shorter sides of the triangle: ').split()
    print('The hypotenuse of the triangle is: {0:.2f}'.format(hypotenuse_calc(int(s1), int(s2))))


# Exercise 59: Coin Flip Simulation - What’s the minimum number of times you have to flip a coin before you can have
# three consecutive flips that result in the same outcome (either all three are heads or all three are tails)? What’s
# the maximum number of flips that might be needed? How many flips are needed on average? In this exercise we will
# explore these questions by creating a program that simulates several series of coin flips. Create a program that uses
# Python’s random number generator to simulate flipping a coin several times. The simulated coin should be fair, meaning
# that the probability of heads is equal to the probability of tails. Your program should flip simulated coins until
# either 3 consecutive heads of 3 consecutive tails occur. Display an H each time the outcome is heads, and a T each
# time the outcome is tails, with all of the outcomes shown on the same line. Then display the number of flips needed to
# reach 3 consecutive flips with the same outcome. When your program is run it should perform the simulation 10 times
# and report the average number of flips needed. Sample output is shown below:

# H  T  H  H  H  (5 flips)
# T  H  T  H  H  T  T  T  (8 flips)
# T  H  H  T  T  T  (6 flips)
# H  T  T  T  (4 flips)
# H  T  T  H  H  H  (6 flips)
# H  H  T  H  H  T  T  H  H  T  H  T  T  H  H  H  (16 flips)
# T  H  T  H  T  T  T  (7 flips)
# T  T  T  (3 flips)
# T  T  H  T  H  T  H  H  H  (9 flips)
# T  H  H  H  (4 flips)
# On average, 6.8 flips were needed for 10 cycles

import random

print('Coin Flip Simulation')
sim_cycles = 10
sim_total_flips = 0
average_total_flips = 0
for i in range(1, sim_cycles + 1):
    flip_try = ''
    flip_counter = 0
    while ' T  T  T ' not in flip_try and ' H  H  H ' not in flip_try:
        flip = random.randint(1, 2)
        if flip == 1:
            flip = ' H '
        else:
            flip = ' T '
        flip_try += flip
        flip_counter += 1
    print(f'{flip_try} ({flip_counter} flips)')
    sim_total_flips += flip_counter
average_total_flips = sim_total_flips / sim_cycles
print(f'On average, {average_total_flips} flips were needed for {sim_cycles} cycles')


# Exercise 58: Maximum Integer - This exercise examines the process of identifying the maximum value in a collection of
# integers. Each of the integers will be randomly selected from the numbers between 1 and 100. The collection of
# integers may contain duplicate values, and some of the integers between 1 and 100 may not be present. Take a moment
# and think about how you would handle this problem on paper. Many people would check each integer in sequence and ask
# hemself if the number that they are currently considering is larger than the largest number that they have seen
# previously. If it is, then they forget the previous maximum number and remember the current number as the new maximum
# number. This is a reasonable approach, and will result in the correct answer when the process is performed carefully.
# While we can answer the question posed at the end of the previous paragraph using probability theory, we are going to
# explore it by simulating the situation. Create a program that begins by selecting a random integer between 1 and 100.
# Save this integer as the maximum number encountered so far. After the initial integer has been selected, generate 99
# additional random integers between 1 and 100. Check each integer as it is generated to see if it is larger than the
# maximum number encountered so far. If it is then your program should update the maximum number encountered and count
# the fact that you performed an update. Display each integer after you generate it. Include a notation with those
# integers which represent a new maximum. After you have displayed 100 integers your program should display the maximum
# value encountered, along with the number of times the maximum value was updated during the process.

import random

print('Maximum Integer')
list = []
update_counter = 0
max = random.randint(1, 100)
print(max)
while len(list) < 99:
    list.append(random.randint(1, 100))
    if list[len(list)-1] > max:
        max = list[len(list)-1]
        print(f'{max} <== Update')
        update_counter += 1
    else:
        print(list[len(list)-1])
print(f'Maximum integer for 100 random integers is {max}, {update_counter} updates performed')


# Exercise 57: Decimal to Binary - Write a program that converts a decimal (base 10) number to binary (base 2). Read the
# decimal number from the user as an integer and then use the division algorithm shown below to perform the conversion.
# When the algorithm completes, result contains the binary representation of the number. Display the result, along with
# an appropriate message.
#
# *Let result be an empty string
# Let q represent the number to convert
# repeat
#     Set r equal to the remainder when q is divided by 2
#     Convert r to a string and add it to the beginning of result
#     Divide q by 2, discarding any remainder, and store the result back into q
# until q is 0*

print('Decimal to Binary')
binary = ''
decimal = int(input('Please enter the number to convert to binary: '))
while decimal != 0:
    r = decimal % 2
    r = str(r)
    binary = r + binary
    decimal = decimal // 2

print(binary)


# Exercise 56: Binary to Decimal - Write a program that converts a binary (base 2) number to decimal (base 10). Your
# program should begin by reading the binary number from the user as a string. Then it should compute the equivalent
# decimal number by processing each digit in the binary number. Finally, your program should display the equivalent
# decimal number with an appropriate message.

print('Binary to Decimal')
decimal = 0
binary = input('Please enter the number to convert to binary: ')
power = 0
for i in binary:
    ii = int(i) * 2 ** power
    decimal += ii
    power += 1

print(decimal)


# Exercise 55: Prime Factors - The prime factorization of an integer, n, can be determined using the following steps:
#
# *Initialize factor to two
# While factor is less than or equal to n do
#     If n is evenly divisible by factor then
#         Conclude that factor is a factor of n
#         Divide n by factor using integer division
#     Else
#         Increase factor by one*
#
# Write a program that reads an integer from the user. If the value entered by the user is less than 2 then your
# program should display an appropriate error message. Otherwise your program should display the prime numbers that
# can be multiplied together to compute n, with one factor appearing on each line.

print('Prime factors')
num = int(input('Enter an integer (2 or greater): '))
f = 2
while num < f:
    print('Integer must be 2 or greater!')
    num = int(input('Enter an integer (2 or greater): '))

while f <= num:
    if num % f == 0:
        num = num / f
        print(f)
    else:
        f += 1
print(num)


# Exercise 54: Greatest Common Divisor  - The greatest common divisor of two positive integers, n and m,
# is the largest number, d, which divides evenly into both n and m. There are several algorithms that can be used to
# solve this problem, including: *Initialize d to the smaller of m and n. While d does not evenly divide m or d does
# not evenly divide n do Decrease the value of d by 1 Report d as the greatest common divisor of n and m*
#
# Write a program that reads two positive integers from the user and uses this algorithm to determine and report
# their greatest common divisor.
#
# Solution 1: with a while loop

print('Greatest Common Divisor')
m, n = input('Please input two positive integers: ').split()
m = int(m)
n = int(n)
d = 0
if m > n:
    d = n
else:
    d = m

while n % d != 0 or m % d != 0:
    d -= 1
print(d)

# Solution 2: with a for loop

print('Greatest Common Divisor')
m, n = input('Please input two positive integers: ').split()
m = int(m)
n = int(n)
d = 0
if m > n:
    d = n
else:
    d = m

for i in range(1, d):
    if n % d == 0 and m % d == 0:
        print(d)
        break
    d -= 1
    

# Exercise 53: Multiplication Table - In this exercise you will create a program that displays a multiplication table
# that shows the products of all combinations of integers from 1 times 1 up to and including 10 times 10. Your
# multiplication table should include a row of labels across the top of it containing the numbers 1 through 10. It
# should also include labels down the left side consisting of the numbers 1 through 10. The expected output from the
# program is shown in the chart. When completing this exercise you will probably find it helpful to be able to print
# out a value without moving down to the next line. This can be accomplished by added end="" as the last parameter to
# your print statement. For example, print("A") will display the letter A and then move down to the next line. The
# statement print("A", end="") will display the letter A without moving down to the next line, causing the next print
# statement to display its result on the same line as the letter A. (check notion.so link for table display)

print('Multiplication Table')
b = 0
print('      ', end='')
for a in range(1, 11):
    print('{:4d}'.format(a), ' ', end='')
print('')
for i in range(1, 11):
    print('{:4d}'.format(i), ' ', end='')
    for a in range(1, 11):
        b = a * i
        print('{:4d}'.format(b), ' ', end='')
    print('')


# Exercise 52:  MultipleWord Palindromes - There are numerous phrases that are palindromes when spacing is ignored.
# Examples include “go dog”, “flee to me remote elf” and “some men interpret nine memos”, among many others. Extend
# your solution to Exercise 72 so that it ignores spacing while determining whether or not a string is a palindrome.
# For an additional challenge, extend your solution so that is also ignores punctuation marks and treats uppercase
# and lowercase letters as equivalent

print('Is the sentence a palindrome?')
sent = input('Please input a combination of words or a sentence to check if it is a palindrome: ').lower()
sent_no_space = ''
for i in sent:
    if i != ' ':
        sent_no_space += i

if sent_no_space == sent_no_space[::-1]:
    print(f'{sent} is a palindrome')
else:
    print(f'{sent} is not palindrome')

# Exercise 51: Exercise 51: Is a String a Palindrome? - A string is a palindrome if it is identical forward and
# backward. For example “anna”, “civic”, “level” and “hannah” are all examples of palindromicwords. Write a program
# that reads a string from the user and uses a loop to determines whether or not it is a palindrome. Display the result,
# including a meaningful output message.

# Solution #1 - simple, sub-optimal using a built-in function:

print('Is it a palindrome?')
word = input('Please input a word to check if it is a palindrome: ')
rev_word = ''
for i in reversed(word):
    rev_word += i
if word == rev_word:
    print(f'{word} is a palindrome')
else:
    print(f'{word} is not a palindrome')

# Solution #2 - a bit more complex, avoiding the reversed function but still sub-optimal as two data structures are
# used:

print('Is it a palindrome?')
word = input('Please input a word to check if it is a palindrome: ')
rev_word = ''
i = 0
for a in word:
    i -= 1
    rev_word += word[i]
if word == rev_word:
    print(f'{word} is a palindrome')
else:
    print(f'{word} is not a palindrome')

# Solution 3 - optimal, using one data structure instead of two, performs a mirror check of one end of the string vs.
# the other end:

print('Is it a palindrome?')
word = input('Please input a word to check if it is a palindrome: ')
word_palindrome = True
for i in range(0, len(word) // 2):
    if word[i] != word[len(word) - i - 1]:
        word_palindrome = False

if word_palindrome:
    print(f'{word} is a palindrome')
else:
    print(f'{word} is not palindrome')

# Solution 4 - using only slicing operator

print('Is it a palindrome?')
word = input('Please input a word to check if it is a palindrome: ')
if word == word[::-1]:
    print(f'{word} is a palindrome')
else:
    print(f'{word} is not palindrome')

# Exercise 50: Exercise 50: Square Root - Write a program that implements Newton’s method to compute and display the
# square root of a number entered by the user. The algorithm for Newton’s method follows:
# Read x from the user
# Initialize guess to x/2
# While guess is not good enough do
#     Update guess to be the average of guess and x/guess
#
# When this algorithm completes, guess contains an approximation of the square root. The quality of the approximation
# depends on how you define “good enough”. In the author’s solution, guess was considered good enough when the absolute
# alue of the difference between guess ∗ guess and x was less than or equal to 10−12.

print("Square Root - Newthon's method")
x = int(input('Input an integer: '))
a = float(x)
for i in range(3):
    x = 0.5 * (x + a / x)

print('{0:.7f}'.format(x))

# Exercise 49: Caesar Cipher - One of the first known examples of encryption was used by Julius Caesar. Caesar needed to
# provide written instructions to his generals, but he didn’t want his enemies  to learn his plans if the message
# slipped into their hands. As result, he developed what later became known as the Caesar Cipher. The idea behind this
# cipher is simple (and as a result, it provides no protection against modern code breaking techniques). Each letter in
# the original message is shifted by 3 places. As a result, A becomes D, B becomes E, C becomes F, D becomes G, etc. The
# last three letters in the alphabet are wrapped around to the beginning: X becomes A, Y becomes B and Z becomes C.
# Non-letter characters are not modified by the cipher. Write a program that implements a Caesar cipher. Allow the user
# to supply the message and the shift amount, and then display the shifted message. Ensure that your program encodes
# both uppercase and lowercase letters. Your program should also support negative shift values so that it can be used
# both to encode messages and decode messages.

print('Caesar Cipher')
new_message = ''
choice = input('Select E for encoding | Select D for decoding: ')
if choice == 'E':
    message = input('Input the message to be encoded: ')
    shift_amount = int(input('Select the shift amount to be applied for the encoding: '))
    for i in message:
        if 'a' <= i <= 'z':
            pos = ord(i) - ord('a')
            pos = (pos + shift_amount) % 26
            new_char = chr(pos + ord('a'))
            new_message += new_char
        elif 'A' <= i <= 'Z':
            pos = ord(i) - ord('A')
            pos = (pos + shift_amount) % 26
            new_char = chr(pos + ord('A'))
            new_message += new_char
        else:
            new_message += i
    print('The encoded message is:', new_message)
if choice == 'D':
    message = input('Input the message to be decoded: ')
    shift_amount = int(input('Select the shift amount to be applied for the decoding: '))
    for i in message:
        if 'a' <= i <= 'z':
            pos = ord(i) - ord('a')
            pos = (pos - shift_amount) % 26
            new_char = chr(pos + ord('a'))
            new_message += new_char
        elif 'A' <= i <= 'Z':
            pos = ord(i) - ord('A')
            pos = (pos - shift_amount) % 26
            new_char = chr(pos + ord('A'))
            new_message += new_char
        else:
            new_message += i
    print('The encoded message is:', new_message)

# Exercise 48: Admission Price - A particular zoo determines the price of admission based on the age of the guest.
# Guests 2 years of age and less are admitted without charge. Children between 3 and 12 years of age cost $14.00.
# Seniors aged 65 years and over cost $18.00. Admission for all other guests is $23.00. Create a program that begins by
# reading the ages of all of the guests in a group from the user, with one age entered on each line. The user will enter
# a blank line to indicate that there are no more guests in the group. Then your program should display the admission
# cost for the group with an appropriate message. The cost should be displayed using two decimal places.

print('Admission Price')
age = input('Please input the age of group members - one per line with space for end: ')
admission_cost = 0
group_count = 0
while age != '':
    age = int(age)
    group_count += 1
    if 3 <= age <= 12:
        admission_cost += 14.00
    elif 13 <= age <= 64:
        admission_cost += 23.00
    elif age >= 65:
        admission_cost += 18.00
    age = input('Please input the age of group members - one per line with space for end: ')

print('Total admission cost for the group of {0} people is {1:.2f}$'.format(group_count, admission_cost))

# Exercise 47: Compute a Grade Point Average - Exercise 36 included a table that shows the conversion from letter grades
# to grade points at a particular academic institution. In this exercise you will compute the grade point average of an
# arbitrary number of letter grades entered by the user. The user will enter a blank line to indicate that all of the
# grades have been provided. For example, if the user enters A, followed by C+, followed by B, followed by a blank line
# then your program should report a grade point average of 3.1. You may find your solution to Exercise 51 helpful when
# completing this exercise. Your program does not need to do any error checking. It can assume that each value entered
# by the user will always be a valid letter grade or a blank line.

print('Letter Grade to Grade Points')
grade = input('Please input your letter grades to calculate their average (use a blank line to finish): ')
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
grade_counter = 0
total_grade = 0
while grade != '':
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
    grade_counter += 1
    total_grade += grade_point
    grade = input('Please input your letter grades to calculate their average (use a blank line to finish): ')

average_grade = total_grade / grade_counter
print(f'Your average grade for your {grade_counter} grades is: {average_grade}')

# Exercise 46: No More Pennies - February 4, 2013 was the last day that pennies were distributed by the Royal Canadian
# Mint. Now that pennies have been phased out retailers must adjust totals so that they are multiples of 5 cents when
# they are paid for with cash (credit card and debit card transactions continue to be charged to the penny). While
# retailers have some freedomin how they do this, most choose to round to the closest nickel. Write a program that reads
# prices from the user until a blank line is entered. Display the total cost of all the entered items on one line,
# followed by the amount due if the customer pays with cash on a second line. The amount due for a cash payment should
# be rounded to the nearest nickel. One way to compute the cash payment amount is to begin by determining how many
# pennies would be needed to pay the total. Then compute the remainder when this number of pennies is divided by 5.
# Finally, adjust the total down if the remainder is less than 2.5. Otherwise adjust the total up.

total = 0
rounded_total = 0
line = input('Please input a all the prices (use a blank line if you are finished): ')
while line != "":
    total += float(line)
    line = input('Please input a all the prices (use a blank line if you are finished): ')

total_transformed = total * 100
pennies_per_nickel = 5

if total_transformed % pennies_per_nickel > 2:
    rounded_total = total_transformed + (pennies_per_nickel - total_transformed % pennies_per_nickel)
else:
    rounded_total = total_transformed - total_transformed % pennies_per_nickel

print('Amount due: {0:.2f}$'.format(total))
print('Amount due in cash: {0:.2f}$'.format(rounded_total / 100))

# Exercise 45: Temperature Conversion Table - Write a program that displays a temperature conversion table for degrees
# Celsius and degrees Fahrenheit. The table should include rows for all temperatures between 0 and 100 degrees Celsius
# that are multiples of 10 degrees Celsius. Include appropriate headings on your columns. The formula for converting
# between degrees Celsius and degrees Fahrenheit can be found on the internet.

print('Temperature conversion table')
temperature_c = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in temperature_c:
    print('Temperature in Celsius: {0:.2f} = {1:.2f} Fahrenheit'.format(i, (i * 9) / 5 + 32))

# Exercise 44: Discount Table - A particular retailer is having a 60 percent off sale on a variety of discontinued
# products. The retailer would like to help its customers determine the reduced price of the merchandise by having a
# printed discount table on the shelf that shows the original prices and the prices after the discount has been applied.
# Write a program that uses a loop to generate this table, showing the original price, the discount amount, and the new
# price for purchases of $4.95, $9.95, $14.95, $19.95 and $24.95. Ensure that the discount amounts and the new prices
# are rounded to 2 decimal places when they are displayed.

print('The discount table display')
prices = input('Please enter a collection of prices to discount: ').split()
discount = input('Please enter the discount % which you want to apply: ')
discount = int(discount)
prices = list(map(float, prices))

for price in prices:
    print('Original price: {0:.2f}$ | Discount: {1:.2f}$ | New price: {2:.2f}$'.format(price, (price * discount) / 100,
                                                                                       (price - (
                                                                                                   price * discount) / 100)))

# Exercise 43: Average - In this exercise you will create a program that computes the average of a collection of values
# entered by the user. The user will enter 0 as a sentinel value to indicate that no further values will be provided.
# Because the 0 marks the end of the input it should not be included in the average.

print('The average calculator')
average_list = input('Please enter a collection of scores without comma to compute the average: ').split()
average_list = list(map(int, average_list))
total = 0
length = len(a)
for i in a:
    total += i
average = total / (length - 1)
print(average)

# Exercise 42: Exercise 42: Roulette Payouts - A roulette wheel has 38 spaces on it. Of these spaces, 18 are black, 18
# are red, and two are green. The green spaces are numbered 0 and 00. The red spaces are numbered 1, 3, 5, 7, 9, 12, 14,
# 16, 18, 19, 21, 23, 25, 27, 30 32, 34 and 36. The remaining integers between 1 and 36 are used to number the black
# spaces. Many different bets can be placed in roulette.We will only consider the following subset of them in this
# exercise:
#
# - Single number (1 to 36, 0, or 00)
# - Red versus Black
# - Odd versus Even (Note that 0 and 00 do not pay out for even)
# - 1 to 18 versus 19 to 36
#
# Write a program that simulates a spin of a roulette wheel by using Python’s random number generator. Display the
# number that was selected and all of the bets that must be payed. For example, if 13 is selected then your program
# should display:
#
# # The spin resulted in 13...
# # Pay 13
# # Pay Black
# # Pay Odd
# # Pay 1 to 18
# If the simulation results in 0 or 00 then your program should display Pay 0 or Pay 00 without any further output.

import random

print('Roulette Payouts')
random_number = random.randint(0, 37)
even_odd_win = ''
color_win = ''
range_win = ''

# define the color win
red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black_numbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
if random_number in red_numbers:
    color_win = 'Red'
elif random_number in black_numbers:
    color_win = 'Black'
else:
    color_win = 'none - 0 / 00 spin'

# define the even / odd win
if random_number == 0 or random_number == 37:
    even_odd_win = 'Odd'
elif random_number % 2 == 0:
    even_odd_win = 'Even'
elif random_number % 2 != 0:
    even_odd_win = 'Odd'

# define range win
if random_number in range(1, 18):
    range_win = '1 to 18'
elif random_number in range(19, 36):
    range_win = '19 to 36'
elif random_number == 0 or random_number == 37:
    range_win = 'none - 0 / 00 spin'

if random_number == 37:
    random_number = '00'
print(f'The spin resulted in {random_number}...')
print(f'Pay {random_number}')
print(f'Pay {color_win}')
print(f'Pay {even_odd_win}')
print(f'Pay {range_win}')

# Exercise 41: Next Day - Write a program that reads a date from the user and computes its immediate successor. For
# example, if the user enters values that represent 2013-11-18 then your program should display a message indicating
# that the day immediately after 2013-11-18 is 2013-11-19. If the user enters values that represent 2013-11-30 then the
# program should indicate that the next day is 2013-12-01. If the user enters values that represent 2013-12-31 then the
# program should indicate that the next day is 2014-01-01. The date will be entered in numeric form with three separate
# input statements; one for the year, one for the month, and one for the day. Ensure that your program works correctly
# for leap years.

print('Next day calendar')
year = int(input('Please select a year: '))
month = int(input('Please select a month: '))
day = int(input('Please select a day: '))

leap_year = False
if year % 400 == 0:
    leap_year = True
elif year % 100 == 0:
    leap_year = False
elif year % 4 == 0:
    leap_year = True
else:
    leap_year = False

next_day = day + 1
if next_day > 31 and month in [1, 3, 5, 7, 8, 10, 12]:
    next_day = 1
elif next_day > 30 and month in [4, 6, 9, 11]:
    next_day = 1
elif next_day > 29 and leap_year:
    next_day = 1
elif next_day > 28 and not leap_year:
    next_day = 1

next_month = month
if next_day == 1:
    next_month += 1
if next_month > 12:
    next_month = 1

next_year = year
if next_month == 1:
    next_year += 1

print(f'Current day is: {day} - {month} - {year}')
print(f'Next day is: {next_day} - {next_month} - {next_year}')

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

# Exercise 39: Cell Phone Bill - A particular cell phone plan includes 50 minutes of air time and 50 text messages
# for $15.00 a month. Each additional minute of air time costs $0.25, while additional text messages cost $0.15 each.
# All cell phone bills include an additional charge of $0.44 to support 911 call centers, and the entire bill (
# including the 911 charge) is subject to 5 percent sales tax. Write a program that reads the number of minutes and
# text messages used in a month from the user. Display the base charge, additional minutes charge (if any),
# additional text message charge (if any), the 911 fee, tax and total bill amount. Only display the additional minute
# and text message charges if the user incurred costs in these categories. Ensure that all of the charges are
# displayed using 2 decimal places.

print('The cell phone invoicing tool')
minutes = int(input('Please input the number of minutes and messages used for the given month: '))
messages = int(input('Please input the number of minutes and messages used for the given month: '))
print('-' * 10)
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
print('=' * 10)
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
    dog_human_age = 21 + ((dog_age - 2) * 4)
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
cents = change * 100

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
total_weight = int(widgets) * widget_weight + int(gizmos) * gizmo_weight
print(f'The total weight of your order is: {total_weight} grams')

# Exercise 6: Sum of the First n Positive Integers - Write a program that reads a positive integer, n,
# from the user and then displays the sum of all of the integers from 1 to n. The sum of the first n positive
# integers can be computed using the formula: sum = (n)(n + 1)/2

print('Sum of all integers from 1 to n')
n = int(input('Supply a positive integer for n: '))
sum_to_n = (n * (n + 1)) / 2
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
