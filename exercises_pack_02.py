# EX. 1 Bank account class and object with instance methods and class-side method which counts the number a class
# instance has been created

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

# EX. 2 Same as above but split into (1) a 'fintech' package / 'accounts' module + (2) main part
# Package 'fintech' / module 'accounts'

"""This is the accounts module from the fintech package"""

class AmountError(Exception):
    '''Amount deposited or deposited must be bigger than 0'''
    def __init__(self, account, message):
        self.account = account
        self.message = message

    def __str__(self):
        return 'AmountError (' + self.message + ') on ' + str(self.account)


class BalanceError(Exception):
    '''Overdraft limit handling error'''

    def __str__(self):
        return 'Overdraft limit exceeded, operation cannot be executed'


class Account:
    instance_count = 0

    @classmethod
    def increment_instance_count(cls):
        cls.instance_count += 1
        print('A new instance has been created')

    def __init__(self, acc_number, acc_holder, open_balance):
        Account.increment_instance_count()
        self.acc_number = acc_number
        self.acc_holder = acc_holder
        self._open_balance = open_balance

    @property
    def open_balance(self):
        return self._open_balance

    @open_balance.setter
    def open_balance(self, new_balance):
        self._open_balance = new_balance

    def deposit(self, amount):
        if amount <= 0:
            raise AmountError(account = self, message = 'Cannot deposit negative amounts')
        else:
            self.open_balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise AmountError(account = self, message = 'Cannot deposit negative amounts')
        else:
            self.open_balance -= amount

    def __str__(self):
        return 'Account[' + str(self.acc_number) + '] - ' + self.acc_holder + ', ' + ' account = ' + str(
            self.open_balance)


class CurrentAccount(Account):
    def __init__(self, acc_number, acc_holder, open_balance, overdraft_limit):
        super().__init__(acc_number, acc_holder, open_balance)
        self.overdraft_limit = overdraft_limit

    def __str__(self):
        return 'Account[' + str(self.acc_number) + '] - ' + self.acc_holder + ', ' + ', account = ' + str(
            self.open_balance) + ', overdraft limit = ' + str(self.overdraft_limit)

    def withdraw(self, amount):
            overdraft_check = self.open_balance - amount
            if amount <= 0:
                raise AmountError(account = self, message = 'Cannot deposit negative amounts')
            elif overdraft_check > self.overdraft_limit:
                self.open_balance -= amount
            else:
                raise BalanceError


class DepositAccount(Account):
    def __init__(self, acc_number, acc_holder, open_balance, interest_rate):
        super().__init__(acc_number, acc_holder, open_balance)
        self.interest_rate = interest_rate

    def interest_rate_apply(self):
        self.open_balance = self.open_balance + self.open_balance * self.interest_rate
        return self.open_balance

    def __str__(self):
        return 'Account[' + str(self.acc_number) + '] - ' + self.acc_holder + ', ' + ', account = ' + str(
            self.open_balance) + ', interest rate = ' + str(self.interest_rate*100) + '%'


class InvestmentAccount(Account):
    def __init__(self, acc_number, acc_holder, open_balance, investment_type):
        super().__init__(acc_number, acc_holder, open_balance)
        self.invetment_type = investment_type

    def __str__(self):
        return 'Account[' + str(self.acc_number) + '] - ' + self.acc_holder + ', ' + ', account = ' + str(
            self.open_balance) + ', investment type = ' + self.invetment_type


# main part below

import fintech.accounts as accounts

acc1 = accounts.CurrentAccount(125343, 'Lea Smith', 25, -100)
print(acc1)
print('-'*10)

try:
    acc1.withdraw(200)
except accounts.BalanceError as b:
    print('Handling exception')
    print(b)

try:
    acc1.withdraw(5)
    print(acc1)
    acc1.deposit(-2)
    print('a')
except accounts.AmountError as e:
    print('Handling exception')
    print(e)
    print(acc1)

try:
    acc2 = accounts.CurrentAccount(23452, 'John Hawk', 13, -100)
    print(acc2)
    acc2.withdraw(3)
    print(acc2)
    acc2.withdraw(-1)
except accounts.AmountError as e:
    print(e)

# EX. 3 Version with ABC for Account class:

# Package 'fintech' / module 'accounts'

"""This is the accounts module from the fintech package"""

from abc import ABCMeta, abstractmethod


class AmountError(Exception):
    '''Amount deposited or deposited must be bigger than 0'''
    def __init__(self, account, message):
        self.account = account
        self.message = message

    def __str__(self):
        return 'AmountError (' + self.message + ') on ' + str(self.account)


class BalanceError(Exception):
    '''Overdraft limit handling error'''

    def __str__(self):
        return 'Overdraft limit exceeded, operation cannot be executed'


class Account(metaclass=ABCMeta):
    instance_count = 0

    @classmethod
    def increment_instance_count(cls):
        cls.instance_count += 1
        print('A new instance has been created')

    def __init__(self, acc_number, acc_holder, open_balance):
        Account.increment_instance_count()
        self.acc_number = acc_number
        self.acc_holder = acc_holder
        self._open_balance = open_balance

    @property
    @abstractmethod
    def open_balance(self):
        pass

    @open_balance.setter
    @abstractmethod
    def open_balance(self, new_balance):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def __str__(self):
        pass


class CurrentAccount(Account):
    def __init__(self, acc_number, acc_holder, open_balance, overdraft_limit):
        super().__init__(acc_number, acc_holder, open_balance)
        self.overdraft_limit = overdraft_limit

    @property
    def open_balance(self):
        return self._open_balance

    @open_balance.setter
    def open_balance(self, new_balance):
        self._open_balance = new_balance

    def withdraw(self, amount):
            overdraft_check = self.open_balance - amount
            if amount <= 0:
                raise AmountError(account = self, message = 'Cannot deposit negative amounts')
            elif overdraft_check > self.overdraft_limit:
                self.open_balance -= amount
            else:
                raise BalanceError

    def deposit(self, amount):
        if amount <= 0:
            raise AmountError(account = self, message = 'Cannot deposit negative amounts')
        else:
            self.open_balance += amount

    def __str__(self):
        return 'Current Account[' + str(self.acc_number) + '] - ' + self.acc_holder + ', ' + ', account = ' + str(
            self.open_balance) + ', overdraft limit = ' + str(self.overdraft_limit)

class DepositAccount(Account):
    def __init__(self, acc_number, acc_holder, open_balance, interest_rate):
        super().__init__(acc_number, acc_holder, open_balance)
        self.interest_rate = interest_rate

    @property
    def open_balance(self):
        return self._open_balance

    @open_balance.setter
    def open_balance(self, new_balance):
        self._open_balance = new_balance

    def interest_rate_apply(self):
        self.open_balance = self.open_balance + self.open_balance * self.interest_rate
        return self.open_balance

    def withdraw(self, amount):
        if amount <= 0:
            raise AmountError(account = self, message = 'Cannot deposit negative amounts')
        else:
            self.open_balance -= amount

    def deposit(self, amount):
        if amount <= 0:
            raise AmountError(account = self, message = 'Cannot deposit negative amounts')
        else:
            self.open_balance += amount

    def __str__(self):
        return 'Deposit Account[' + str(self.acc_number) + '] - ' + self.acc_holder + ', ' + ', account = ' + str(
            self.open_balance) + ', interest rate = ' + str(self.interest_rate*100) + '%'


class InvestmentAccount(Account):
    def __init__(self, acc_number, acc_holder, open_balance, investment_type):
        super().__init__(acc_number, acc_holder, open_balance)
        self.invetment_type = investment_type

    @property
    def open_balance(self):
        return self._open_balance

    @open_balance.setter
    def open_balance(self, new_balance):
        self._open_balance = new_balance

    def withdraw(self, amount):
        if amount <= 0:
            raise AmountError(account = self, message = 'Cannot deposit negative amounts')
        else:
            self.open_balance -= amount

    def deposit(self, amount):
        if amount <= 0:
            raise AmountError(account = self, message = 'Cannot deposit negative amounts')
        else:
            self.open_balance += amount

    def __str__(self):
        return 'Investment Account[' + str(self.acc_number) + '] - ' + self.acc_holder + ', ' + ', account = ' + str(
            self.open_balance) + ', investment type = ' + self.invetment_type

# Main part (not part of the 'fintech' package

import fintech.accounts as accounts

acc1 = accounts.CurrentAccount('123', 'John', 10.05, 100.0)
acc2 = accounts.DepositAccount('345', 'John', 23.55, 0.5)
acc3 = accounts.InvestmentAccount('567', 'Phoebe', 12.45, 'risky')

print(acc1)
print(acc2)
print(acc3)

acc1.deposit(10)
acc2.withdraw(3.55)
acc3.deposit(1000)

print(acc1)
print(acc2)
print(acc3)

# EX. 4 Version with ABC and 'timer' decorator (with arguments) in the sub-classes:

# Package 'fintech' / module 'accounts'

"""This is the accounts module from the fintech package"""

from abc import ABCMeta, abstractmethod

from timeit import default_timer


def timer(func):
    def inner(x, y):
        start = default_timer()
        func(x, y)
        end = default_timer()
        print('returned from ', func, 'it took', end - start, 'seconds')
    return inner


class AmountError(Exception):
    '''Amount deposited or deposited must be bigger than 0'''
    def __init__(self, account, message):
        self.account = account
        self.message = message

    def __str__(self):
        return 'AmountError (' + self.message + ') on ' + str(self.account)


class BalanceError(Exception):
    '''Overdraft limit handling error'''

    def __str__(self):
        return 'Overdraft limit exceeded, operation cannot be executed'


class Account(metaclass=ABCMeta):
    instance_count = 0

    @classmethod
    def increment_instance_count(cls):
        cls.instance_count += 1
        print('A new instance has been created')

    def __init__(self, acc_number, acc_holder, open_balance):
        Account.increment_instance_count()
        self.acc_number = acc_number
        self.acc_holder = acc_holder
        self._open_balance = open_balance

    @property
    @abstractmethod
    def open_balance(self):
        pass

    @open_balance.setter
    @abstractmethod
    def open_balance(self, new_balance):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def __enter__(self):
        print('__enter__')
        return self

    def __exit__(self, *args):
        print('__exit__:', args)
        return False

    def __getattr__(self, attribute):
        print('__getattr__: unknown attribute accessed - ', attribute)
        return '-1'

    @abstractmethod
    def __str__(self):
        pass


class CurrentAccount(Account):
    def __init__(self, acc_number, acc_holder, open_balance, overdraft_limit):
        super().__init__(acc_number, acc_holder, open_balance)
        self.overdraft_limit = overdraft_limit

    @property
    def open_balance(self):
        return self._open_balance

    @open_balance.setter
    def open_balance(self, new_balance):
        self._open_balance = new_balance

    @timer
    def withdraw(self, amount):
            overdraft_check = self.open_balance - amount
            if amount <= 0:
                raise AmountError(account = self, message = 'Cannot deposit negative amounts')
            elif overdraft_check > self.overdraft_limit:
                self.open_balance -= amount
            else:
                raise BalanceError

    @timer
    def deposit(self, amount):
        if amount <= 0:
            raise AmountError(account = self, message = 'Cannot deposit negative amounts')
        else:
            self.open_balance += amount

    def __str__(self):
        return 'Current Account[' + str(self.acc_number) + '] - ' + self.acc_holder + ', ' + ', account = ' + str(
            self.open_balance) + ', overdraft limit = ' + str(self.overdraft_limit)

class DepositAccount(Account):
    def __init__(self, acc_number, acc_holder, open_balance, interest_rate):
        super().__init__(acc_number, acc_holder, open_balance)
        self.interest_rate = interest_rate

    @property
    def open_balance(self):
        return self._open_balance

    @open_balance.setter
    def open_balance(self, new_balance):
        self._open_balance = new_balance

    def interest_rate_apply(self):
        self.open_balance = self.open_balance + self.open_balance * self.interest_rate
        return self.open_balance

    @timer
    def withdraw(self, amount):
        if amount <= 0:
            raise AmountError(account = self, message = 'Cannot deposit negative amounts')
        else:
            self.open_balance -= amount

    @timer
    def deposit(self, amount):
        if amount <= 0:
            raise AmountError(account = self, message = 'Cannot deposit negative amounts')
        else:
            self.open_balance += amount

    def __str__(self):
        return 'Deposit Account[' + str(self.acc_number) + '] - ' + self.acc_holder + ', ' + ', account = ' + str(
            self.open_balance) + ', interest rate = ' + str(self.interest_rate*100) + '%'


class InvestmentAccount(Account):
    def __init__(self, acc_number, acc_holder, open_balance, investment_type):
        super().__init__(acc_number, acc_holder, open_balance)
        self.invetment_type = investment_type

    @property
    def open_balance(self):
        return self._open_balance

    @open_balance.setter
    def open_balance(self, new_balance):
        self._open_balance = new_balance

    @timer
    def withdraw(self, amount):
        if amount <= 0:
            raise AmountError(account = self, message = 'Cannot deposit negative amounts')
        else:
            self.open_balance -= amount

    @timer
    def deposit(self, amount):
        if amount <= 0:
            raise AmountError(account = self, message = 'Cannot deposit negative amounts')
        else:
            self.open_balance += amount

    def __str__(self):
        return 'Investment Account[' + str(self.acc_number) + '] - ' + self.acc_holder + ', ' + ', account = ' + str(
            self.open_balance) + ', investment type = ' + self.invetment_type

# Main part (not part of the 'fintech' package

import fintech.accounts as accounts

acc1 = accounts.CurrentAccount('123', 'John', 10.05, -100.0)
print(acc1)
acc1.deposit(22)
print(acc1)
acc1.withdraw(5)
print(acc1)