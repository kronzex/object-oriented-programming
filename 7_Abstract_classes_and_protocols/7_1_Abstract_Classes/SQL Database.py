"""
Task: SQL Database

Description:
A database base class defined as an abstract class, containing the following abstract methods:

 ➖ connect
 ➖ disconnect
 ➖ execute

Create the classes `MySQLDatabase` and `PostgreSQLDatabase` that inherit this base database class and implement its abstract methods.
Each class must implement a `connect` method to establish a connection to the respective database, a `disconnect` method to terminate the connection, and an `execute` method to perform a query against the corresponding database.

Inside the MySQLDatabase class:

 ➖ The connect method should print the message "Connecting to the MySQL database..." to the screen.

 ➖ The disconnect method should print the message "Disconnecting from the MySQL database..." to the screen.

 ➖ The execute method should accept a database query as a string and print the message "Executing query '{query}' in the MySQL database..." to the screen.

Inside the PostgreSQLDatabase class:

 ➖ The connect method should print the message "Connecting to the PostgreSQL database..." to the screen.

 ➖ The disconnect method should print the message "Disconnecting from the PostgreSQL database..." to the screen.

 ➖ The execute method should accept a database query as a string and print the message "Executing query '{query}' in the PostgreSQL database..." to the screen.

"""

from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def disconnect(self):
        pass
    @abstractmethod
    def execute(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        print('Connecting to MySQL database...')

    def disconnect(self):
        print('Disconnecting from MySQL database...')

    def execute(self, query):
        print(f'''Executing query '{query}' in MySQL database...''')


class PostgreSQLDatabase(Database):
    def connect(self):
        print('Connecting to PostgreSQL database...')

    def disconnect(self):
        print('Disconnecting from PostgreSQL database...')

    def execute(self, query):
        print(f'''Executing query '{query}' in PostgreSQL database...''')




# below Code for testing

mysql_db = MySQLDatabase()
postgresql_db = PostgreSQLDatabase()

mysql_db.connect()
mysql_db.execute(
    "SELECT * FROM customers;")
mysql_db.disconnect()

postgresql_db.connect()
postgresql_db.execute(
    "SELECT * FROM customers;")
postgresql_db.disconnect()




