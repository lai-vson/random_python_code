import datetime

user_year = 0
user_month = 0
user_day = 0
date_info_user = ''
user_respond = ''

def check():
    global user_year, user_month, user_day, date_info_user

    if date_info_user == '1':
        x = datetime.datetime(user_year, 12, 31)
        if x.strftime('%j') == '366':
            print('Leap year')
        else:
            print('Not leap year')
    elif date_info_user == '2':
        x = datetime.datetime(user_year, user_month, user_day)
        print('{} {}, {} is {}'.format(user_day, x.strftime('%b'), user_year, x.strftime('%A')))
    elif date_info_user == '3':
        x = datetime.datetime(user_year, user_month, user_day)
        print('{} {}, {} is Week {}'.format(user_day, x.strftime('%b'), user_year, x.strftime('%U')))

    while True:
        print('Next query? \'yes\' to continue or \'q\' to quit.')
        user_respond = input(': ')
        
        if user_respond == 'yes' or user_respond == 'y':
            date_info()
        elif user_respond == 'q':
            quit()


def user_input_1():
    global user_year, user_day, user_month, date_info_user

    if date_info_user == '1':
        user_year = int(input('Input year: '))
    elif date_info_user == '2' or '3':
        user_year = int(input('Input year: '))

        user_month = int(input('Input month (1-12): '))
        while user_month not in range(1, 12):
            user_month = int(input('Input month (1-12): '))

        user_day = int(input('Input day (1-31): '))
        while user_day not in range(1, 31):
            user_day = int(input('Input day (1-31): '))
    else:
        print('Key in 1-3 only')
        date_info()

    check()

def date_info():
    global date_info_user

    print('What kind of information would you like to check?')
    print('1. Is it leap year?')
    print('2. What day is it on that date?')
    print('3. What is the week number?')
    date_info_user = input(': ')
    user_input_1()

if __name__ == '__main__':
    date_info()
