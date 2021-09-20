user_name = input('Name: ')
user_age = int(input('Age: '))
user_country = input('From: ')
user_hobbies = input('Hobby: ')

def story():
    print('My name is {}.\nI am {} years old.\nI come from {}.\nMy hobby is {}.'.format(user_name, user_age, user_country, user_hobbies))
    return

if __name__ == '__main__':
    story()
