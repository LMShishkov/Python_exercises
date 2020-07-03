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
