"""
Task: Password Invalid Error


Description:
For the next task, we need to implement a base exception class called `PasswordInvalidError`, which inherits from the standard `Exception` class. This class can be used to handle any general errors related to invalid passwords.

The following classes should inherit from it:

 ➖ `PasswordLengthError` — represents an error related to an insufficient password length;

 ➖ `PasswordContainUpperError` — represents an error related to the absence of uppercase letters in the password;

 ➖ `PasswordContainDigitError` — represents an error related to the absence of digits in the password.

Create a `User` class with `username` and `password` attributes (with `password` defaulting to `None`). The class should include a `set_password` method that accepts a password and assigns it to the `password` attribute.
The `set_password` method must also verify that the password meets the following security requirements:

 ➖The password must be at least 8 characters long (otherwise, a `PasswordLengthError` exception is raised with the message "Password must be at least 8 characters long");

 ➖ The password must contain at least one uppercase letter (otherwise, a `PasswordContainUpperError` exception is raised with the message "Password must contain at least one uppercase letter");

 ➖ The password must contain at least one digit (otherwise, a PasswordContainDigitError exception is raised with the message "The password must contain at least one digit");
"""

class PasswordInvalidError(Exception):
    pass

class PasswordLengthError(PasswordInvalidError):
    pass

class PasswordContainUpperError(PasswordInvalidError):
    pass
class PasswordContainDigitError(PasswordInvalidError):
    pass

class User:

    def __init__(self, username, password=None):
        self.username = username
        if password is not None:
            self.set_password(password)
        else:
            self.password = None


    def set_password(self, password):
        if len(password) < 8:
           raise PasswordLengthError('Password must be at least 8 characters long')
        list_upper = len([i for i in password if i.isupper()])
        list_digit = len([i for i in password if i.isdigit()])

        if not list_upper:
            raise PasswordContainUpperError('Password must contain at least one uppercase letter"')
        if not list_digit:
            raise PasswordContainDigitError('The password must contain at least one digit')

        self.password = password

# Напишите определение класса User и классов исключений


# Ниже код для проверки


assert issubclass(PasswordInvalidError, Exception)
assert issubclass(PasswordLengthError, PasswordInvalidError)
assert issubclass(PasswordContainUpperError, PasswordInvalidError)
assert issubclass(PasswordContainDigitError, PasswordInvalidError)

user = User("johndoe")

try:
    user.set_password("weakpwd")
except PasswordLengthError as e:
    print(e)

try:
    user.set_password("strongpassword8")
except PasswordContainUpperError as e:
    print(e)

try:
    user.set_password("Safepassword")
except PasswordContainDigitError as e:
    print(e)

user.set_password("SecurePass123")
assert user.password == 'SecurePass123'




