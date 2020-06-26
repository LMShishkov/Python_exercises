class Account:
    instance_count = 0

    @classmethod
    def increment_instance_count(cls):
        cls.instance_count += 1
        print('A new instance has been created')

    def __init__(self, acc_number, acc_holder, acc_type, open_balance):
        Account.increment_instance_count()
        self.acc_number = acc_number
        self.acc_holder = acc_holder
        self.acc_type = acc_type
        self.open_balance = open_balance

    def deposit(self, amount):
        self.open_balance += amount

    def withdraw(self, amount):
        self.open_balance -= amount

    def get_balance(self):
        return self.open_balance

    def __str__(self):
        return 'Account[' + str(self.acc_number) + '] - ' + self.acc_holder + ', ' + self.acc_type + ' account = ' + str(
            self.open_balance)


acc1 = Account(120686, 'John Smith', 'current', 10.05)
acc2 = Account(345864, 'John Johnes', 'savings', 23.55)
acc3 = Account(567120, 'Phoebe Phoenix', 'investment', 12.45)

print(acc1)
print(acc2)
print(acc3)

acc1.deposit(23.45)
acc1.withdraw(12.33)
print('balance:', acc1.get_balance())
print('Number of instances created:', Account.instance_count)