# Exercise 2: Area of a Room - Write a program that asks the user to enter the width and length of a room. Once the
# values have been read, your program should compute and display the area of the room. The length and the width will
# be entered as floating point numbers. Include units in your prompt and output message; either feet or meters,
# depending on which unit you are more comfortable working with.

print('This is the room area calculator')
room_width = float(input('Please enter the width of your room in meters: '))
room_length = float(input('Please enter the length of your room in meters: '))
room_area = room_width * room_length
print(f'Your room area is {room_area} square meters')


# Exercise 1: Hello - Write a program that asks the user to enter his or her name. The program should respond with a
# message that says hello to the user, using his or her name.

user_name = input('What is your name? ')
print(f'Hello {user_name}!')
