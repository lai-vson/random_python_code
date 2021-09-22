input_list = []

def user_input():
    global input_list
    user_no_input = input('How many numbers for calculation: ')

    while user_no_input.isnumeric() != True:
        print('Numbers only')
        user_no_input = input('How many numbers for calculation: ')

    user_no_input = int(user_no_input)

    for no_number in range(1, user_no_input + 1):
        input_1 = input('Number ' + str(no_number) + ': ')
        if input_1 == 'q':
            print('Quit')
            quit()
        while input_1.isnumeric() != True:
            print('Calculations for numbers only!')
            input_1 = input('Number ' + str(no_number) + ': ')
            if input_1 == 'q':
                print('Quit')
                quit()
        input_list.append(input_1)

def calculator():
    total_sum = 0.0

    print('Set of number will be calculated: {}'.format(input_list))
    print('Please select type of calculation:-')
    print('-'*30)
    print('+ - Addition')
    print('- - Subtract')
    print('* - Multiply')
    print('/ - Divide')
    print('-' * 30)
    user_respond = input(': ')

    if user_respond == '+':
        for no_number in range(len(input_list)):
            # print(input_list[no_number])
            total_sum += int(input_list[no_number])
        print('The final answer would be: {}'.format(total_sum))
    elif user_respond == '-':
        for no_number in range(len(input_list)):
            # print(input_list[no_number])
            total_sum -= int(input_list[no_number])
        print('The final answer would be: {}'.format(total_sum))
    elif user_respond == '*':
        for no_number in range(len(input_list)):
            # print(input_list[no_number])
            if total_sum == 0:
                total_sum = 1
            total_sum = total_sum * int(input_list[no_number])
        print('The final answer would be: {}'.format(total_sum))
    elif user_respond == '/':
        for no_number in range(len(input_list)):
            # print(input_list[no_number])
            if total_sum == 0:
                total_sum = float(input_list[no_number])
                total_sum = total_sum / int(input_list[no_number+1])
                # print(total_sum)
                continue
            if len(input_list) == (no_number + 2):
                total_sum = total_sum / int(input_list[no_number+1])
                # print(total_sum)
                break
            else:
                total_sum = total_sum / int(input_list[no_number + 1])
                # print(total_sum)
        print('The final answer would be: {}'.format(total_sum))
    elif user_respond == 'q':
        quit()
    else:
        print('ERROR: Please key in the correct operators')
        calculator()

if __name__ == '__main__':
    user_input()
    calculator()
