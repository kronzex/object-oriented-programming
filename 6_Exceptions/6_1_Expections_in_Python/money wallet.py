"""
Task: Mixin for access


Description:
Implement a `Wallet` class—analogous to a physical wallet—that stores information about the currency and the remaining balance of funds in the account. This class should include the following implementations:

 ➖ The `__init__` method creates the attributes `currency` and `balance`. The values for these attributes are provided when the `__init__` method is called. The `currency` attribute must be a string consisting exclusively of three uppercase letters. To ensure this, you must perform the following checks in the specified order:

    If the value provided is not a string, raise a `TypeError` with the message "Invalid currency type".
    If the provided string does not have a length of exactly three characters, raise a `NameError` with the message "Invalid currency name length".
    If the string does not consist solely of uppercase letters, raise a `ValueError` with the message "The name must consist only of uppercase letters".

 ➖ The `__eq__` method, to allow for the comparison of wallet balances. Comparison is only permitted between wallets with the same currency.

    If the currencies differ, a `ValueError` exception must be raised with the message "Cannot compare different currencies".
    If an attempt is made to compare a `Wallet` instance with other types of objects, a `TypeError` exception must be raised with the message "Wallet does not support comparison with <object>".

 ➖ Implement the `__add__` and `__sub__` methods to allow for the addition and subtraction of wallets. Addition and subtraction are only permitted with another instance of the `Wallet` class, and only if their currencies (the `currency` attribute) match. The result of such an operation must be a new `Wallet` instance with the same currency as the operands, and a balance equal to the sum or difference of their respective balances (the balance may become negative in the case of subtraction).

    If an attempt is made to perform an operation with an object that is not an instance of `Wallet`, or if the currencies of the objects do not match, a `ValueError` exception must be raised with the message "This operation is not permitted."
"""

class Wallet:
    def __init__(self, currency, balance):
        if type(currency) != str:
            raise TypeError("Invalid currency type")

        if len(currency) != 3:
            raise NameError('Invalid currency name length')

        if not currency.isupper():
            raise ValueError('The name must consist only of uppercase letters')

        self.currency = currency
        self.balance = balance

    def __eq__(self, other):
        if not isinstance(other, Wallet):
            raise TypeError(f'Wallet does not support comparison with {other}')

        if not self.currency == other.currency:
            raise ValueError('Cannot compare different currencies')

        return self.balance == other.balance


    def __add__(self, other):
        if not isinstance(other, Wallet) or not self.currency == other.currency:
            raise ValueError('This operation is not permitted.')

        return Wallet(self.currency ,self.balance + other.balance)

    def __sub__(self, other):
        if not isinstance(other, Wallet) or not self.currency == other.currency:
            raise ValueError('This operation is not permitted.')

        return Wallet(self.currency ,self.balance - other.balance)



wallet1 = Wallet('USD', 50)
wallet2 = Wallet('RUB', 100)
wallet3 = Wallet('RUB', 150)
wallet4 = Wallet(12, 150)  # исключение TypeError('Неверный тип валюты')
wallet5 = Wallet('qwerty', 150)  # исключение NameError('Неверная длина названия валюты')
wallet6 = Wallet('abc', 150)  # исключение ValueError('Название должно состоять только из заглавных букв')
print(wallet2 == wallet3)  # False
print(wallet2 == 100)  # TypeError('Wallet не поддерживает сравнение с 100')
print(wallet2 == wallet1)  # ValueError('Нельзя сравнить разные валюты')
wallet7 = wallet2 + wallet3
print(wallet7.currency, wallet7.balance)  # печатает 'RUB 250'
wallet2 + 45  # ValueError('Данная операция запрещена')












