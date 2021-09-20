import random

random_num = random.randint(0, 101)  # generate random number

num_guess = int(input('Number of guesses: '))
input_user = int(input('Please guess a number between 0 - 100: '))  # User to input integer


def check(input_user):
    lower_limit = 0
    upper_limit = 100

    while random_num != input_user:
        for x in range(1, num_guess + 1):
            if x < num_guess:
                if input_user > random_num:
                    upper_limit = input_user
                    input_user = int(input(str(lower_limit) + ' - ' + str(upper_limit) + ': '))
                    if input_user > upper_limit:
                        input_user = int(
                            input('Please make sure is within the limit of ' + str(lower_limit) + ' - ' + str(upper_limit) + ': '))
                elif input_user < random_num:
                    lower_limit = input_user
                    input_user = int(input(str(lower_limit) + ' - ' + str(upper_limit) + ': '))
                    if input_user < lower_limit:
                        input_user = int(input('Please make sure is within the limit of ' + str(lower_limit) + ' - ' + str(upper_limit) + ': '))
            elif x == num_guess:
                print('Sorry, try again next time')
        break
    return input_user


if __name__ == '__main__':
    check(input_user)
