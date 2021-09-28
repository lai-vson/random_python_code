import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root')

mycursor = db.cursor()

print('1. To create new database')
print('2. To delete database')
print('3. To list out all database')

user_respond = int(input(': '))


def user_number():
    global user_respond
    if user_respond == 1:
        dbname = input(f'Database name: ')
        try:
            mycursor.execute(f'CREATE DATABASE {dbname}')
            print('Successfully added')
        except:
            print('Error adding database')
    elif user_respond == 2:
        dbname = input('Database name: ')
        try:
            mycursor.execute(f'DROP DATABASE {dbname}')
            print('Successfully delete database')
        except:
            print('Error delete database')
    elif user_respond == 3:
        mycursor.execute('SHOW DATABASES')
        for list in mycursor:
            print(list[0])


if __name__ == '__main__':
    user_number()
