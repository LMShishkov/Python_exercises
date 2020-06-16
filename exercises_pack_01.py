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