"""
Task: Mixin for access

Description:
In an operating system, permissions are access rights that define what actions can be performed within the system. Permissions can restrict the use of specific software, access to files, and security settings.
Let’s create a mixin that simulates access rights management.

To do this, create a class called `PermissionMixin` that includes the following method:

    `__init__(self)`: an initialization method that creates a `permissions` set to store access rights.
    We will use this to keep track of the actions available to users—for example, Read, Write, Execute, etc.

    grant_permission(self, permission): a method for assigning a permission. It adds the provided permission to the `permissions` set.

    revoke_permission(self, permission): a method for revoking a permission. It removes the provided permission from the `permissions` set.

    has_permission(self, permission): a method for checking whether a permission exists. It returns `True` if the provided permission is present in the `permissions` set, and `False` otherwise.


Create a `User` class that inherits from `PermissionMixin` and has the following attributes:
    name: the user's name.
    email: the user's email.
"""


class PermissionMixin:
    def __init__(self, permissions=None):
        self.permissions = set(permissions) if permissions else set()

    def grant_permission(self, permission):
        self.permissions.add(permission)

    def revoke_permission(self, permission):
        self.permissions.discard(permission)

    def has_permission(self, permission):
        return permission in self.permissions

class User(PermissionMixin):
    def __init__(self, name, email, permissions=None):
        super().__init__(permissions)
        self.name = name
        self.email = email

# Below is the code for testing the PermissionMixin.

user1 = User('Alice', 'alice@example.com')
user2 = User('Bob', 'bob@example.com')

assert user1.email == 'alice@example.com'
assert user1.name == 'Alice'
assert user1.permissions == set()

assert user2.email == 'bob@example.com'
assert user2.name == 'Bob'
assert user2.permissions == set()

user1.grant_permission('read')
user1.grant_permission('write')
user2.grant_permission('read')
assert user1.permissions == {'read', 'write'}
assert user2.permissions == {'read'}

assert user1.has_permission('read') is True
assert user1.has_permission('write') is True
assert user1.has_permission('execute') is False

assert user2.has_permission('read') is True
assert user2.has_permission('write') is False
assert user2.has_permission('execute') is False

user1.revoke_permission('write')
user1.revoke_permission('execute')

assert user1.has_permission('read') is True
assert user1.has_permission('write') is False
assert user1.has_permission('execute') is False

print('Good')



