# EX. 1 Calculate down payment of a house which costs $1m, based on the credit rating:

price = 1000000
credit_rating = input('Is your credit rating good? True or False?: ')
if credit_rating == 'True':
    down_payment = price*0.15
if credit_rating == 'False':
    down_payment = price*0.275
print(f"Down payment: ${down_payment}")