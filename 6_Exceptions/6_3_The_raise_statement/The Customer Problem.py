"""
Task: "The Customer" Problem


Description:
Your task is to create a `Customer` class that includes:

1. an `__init__` method that takes a user's name and an optional account balance argument (defaulting to 0). These values should be stored as the attributes `name` and `balance`;

2. a static method `check_type` that accepts a single value. If the value is not a number (i.e., it is not an instance of `int` or `float`), it should raise a `TypeError` with the message: 'The bank works only with numbers'.
The `check_type` method should perform no other actions—it should only raise an exception if the type is incorrect and should not return any value.

3. The `withdraw` method takes a value to be deducted as an argument. First, use the `check_type` method to verify the type of the provided value.
If no exceptions are raised, check whether the customer has sufficient funds in their balance. If there are enough funds, decrease the balance by the specified amount. If there are insufficient funds, raise a `ValueError('The withdrawal amount exceeds the balance.')` exception.

4. The `deposit` method takes a value to be added to the balance as an argument. Use the `check_type` method to verify that the provided value is a number. If no exceptions are raised, increase the customer's balance by the specified amount.

"""



class Customer:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    @staticmethod
    def check_type(check):
        if not isinstance(check, (int, float)):
            raise TypeError('The bank works only with numbers')

    def withdraw(self, amount):
        self.check_type(amount)
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError('The withdrawal amount exceeds the balance.')

    def deposit(self, amount):
        self.check_type(amount)
        self.balance += amount



# Below is the code for testing the Client class


assert Customer.check_type(2) is None, 'The check_type method should not return anything.'
assert Customer.check_type(2.5) is None, 'The check_type method should not return anything.'

for i in ['hello', [1, 2, 3], dict(), set()]:
    try:
        Customer.check_type(i)
    except TypeError as error:
        print(error)
    else:
        raise TypeError(f'The check_type method should throw an error if passed {i}')

bob = Customer('Bob Odenkirk')
assert bob.balance == 0
assert bob.name == 'Bob Odenkirk'
try:
    bob.deposit('hello')
except TypeError as error:
    print(error)
else:
    raise ValueError("You cannot add a string to the balance account.")

try:
    bob.deposit([])
except TypeError as error:
    print(error)
else:
    raise ValueError("You cannot add a list to the balance account.")

bob.deposit(200)
assert bob.balance == 200

try:
    bob.withdraw(300)
except ValueError as e:
    print(e)
else:
    raise ValueError("Check the charge applied when the limit is exceeded")

bob.withdraw(150)
assert bob.balance == 50

terk = Customer('Terk', 1000)
assert terk.name == 'Terk'
assert terk.balance == 1000
terk.withdraw(999)
assert terk.balance == 1, 'The funds were not deducted; please check the transaction.'
terk.withdraw(1)
assert terk.balance == 0, 'The funds were not deducted; please check the transaction.'

try:
    terk.withdraw(1)
except ValueError as e:
    print(e)
else:
    raise ValueError("Check the charge applied when the limit is exceeded")
assert terk.balance == 0




