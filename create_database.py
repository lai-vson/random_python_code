import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root')

mycursor = db.cursor()

class Database:
    def __init__(self, dbname):
        self.dbname = dbname

    def db_add(self):
        try:
            mycursor.execute(f'CREATE DATABASE {self.dbname}')
            print('Successfully added')
        except:
            print('Error adding database')

    def db_delete(self):
        try:
            mycursor.execute(f'DROP DATABASE {self.dbname}')
            print('Successfully delete database')
        except:
            print('Error delete database')

    def db_list(self):
        mycursor.execute('SHOW DATABASES')
        for list in mycursor:
            print(list[0])

if __name__ == '__main__':
    print('1. To create new database')
    print('2. To delete database')
    print('3. To list out all database')
    user_respond = int(input(': '))

    if user_respond == 1:
        mydb = Database(input('Name: '))
        mydb.db_add()
    elif user_respond == 2:
        mydb = Database(input('Name: '))
        mydb.db_delete()
    elif user_respond == 3:
        mydb.db_list()

