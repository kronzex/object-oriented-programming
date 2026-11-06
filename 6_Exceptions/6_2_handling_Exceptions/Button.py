"""
Task: Button
➖

Description:
Your task is to create a `CustomButton` class that includes:

 1. an `__init__` method that accepts one mandatory argument—the button text—which must be stored in an attribute named `text`. The method may also accept any number of keyword arguments; these must be stored as instance attributes using the same names;

 2. a `config` method that accepts an arbitrary number of keyword arguments. It should create an attribute for each provided name—or, if that attribute already exists on the instance, update it to the new value.

 3. The `click` method should execute the following line:

    self.command()

  Here, `command` is not a method, but an attribute that is being called. When this line is executed, two potential issues may arise:

  ➖ the `command` attribute might be missing from the instance, which will trigger an `AttributeError`;

  ➖ the `command` attribute might not support the call operation, which will trigger a `TypeError`.

  You need to handle these situations using a `try-except` block. In the first case, output the message "Button not configured"; in the second case, output "Button broken".

To solve the task, provide only the implementation of the `CustomButton` class.

"""


class CustomButton:
    def __init__(self, text, **kwargs):
        self.text = text
        for key, value in kwargs.items():
            setattr(self, key, value)


    def config(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def click(self):
        try:
            return self.command()
        except AttributeError:
            print('Button not configured')
        except TypeError:
            print('Button broken')


