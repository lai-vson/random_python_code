from tabulate import tabulate

user_num_1 = 0
user_num_2 = 0
total_num = 0
user_respond = ''
user_respond_1 = ''
calculation_list =[]
calculation_history = [user_num_1, user_respond, user_num_2, total_num]

def calculator():

    global user_num_1, user_num_2, total_num, user_respond, user_respond_1, calculation_history

    while True:
        calculation_1()

        if user_respond_1 == 'yes' or user_respond_1 == 'y':
                calculate_history()
                continue

        elif user_respond_1 == 'q':
            calculate_history()
            print(tabulate(calculation_list, headers=['No.', '1st number', 'operator', '2nd number', 'Result'],
                           showindex='always',tablefmt='grid',disable_numparse=True,stralign='center'))
            quit()

        else:
            calculate_history()
            while user_respond_1 != 'yes' and user_respond_1 != 'y':
                print('\'yes\' or \'y\' to continue\n\'q\' to quit')
                user_respond_1 = input(': ')
            continue



def calculation_1():

    global user_num_1, user_num_2, total_num, calculation_history, user_respond_1, user_respond

    number_1()
    while user_num_1.isnumeric() != True:
        print('Number Only')
        number_1()

    user_num_1 = float(user_num_1)

    number_2()
    while user_num_2.isnumeric() != True:
        print('Number Only')
        number_2()

    user_num_2 = float(user_num_2)

    print('Please select the type of operators:-')
    print('*'*30)
    print('(+, -, *, /)')
    print('*'*30)
    user_respond = input(': ')

    if user_respond == '+':
        total_num = user_num_1 +  user_num_2
    elif user_respond == '-':
        total_num = user_num_1 - user_num_2
    elif user_respond == '*':
        total_num = user_num_1 * user_num_2
    elif user_respond == '/':
        total_num = user_num_1 / user_num_2
    print('The answer is {}'.format(total_num))

    user_respond_1 = input('Do you want to continue? If yes, please key in number or "q" to quit.\n: ')

def calculate_history():
    global calculation_history, user_num_1, user_num_2, total_num, calculation_list, user_respond

    calculation_history = [user_num_1, user_respond, user_num_2, total_num]
    calculation_list.append(calculation_history)


def number_1():
    global user_num_1
    user_num_1 = input('Number 1: ')
    return

def number_2():
    global user_num_2
    user_num_2 = input('Number 2: ')
    return


if __name__ == '__main__':
    calculator()
