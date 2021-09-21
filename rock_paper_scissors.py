import random
from tabulate import tabulate

def game():
    users_score = 0
    computer_score = 0
    score_list = []
    score_table = []

    no_round = int(input('No. of round: '))


    for x in range(1, no_round + 1):
        if x < (no_round + 1):
            users_input = input('Rock, Paper, Scissors: ')
            computer_input = random.choice(['Rock', 'Paper', 'Scissors'])
            print('Opponent: ', computer_input)

            users_input = users_input.lower()

            while (users_input == 'rock' and computer_input == 'Rock') or (users_input == 'paper' and computer_input == 'Paper') or (users_input == 'scissors' and computer_input == 'Scissors'):
                users_input = input('Please kindly re-input your choices (Rock, Paper,Scissors): ')
                computer_input = random.choice(['Rock', 'Paper', 'Scissors'])
                print('Opponent: ', computer_input)

            if (users_input == 'rock' and computer_input == 'Scissors') or (users_input == 'paper' and computer_input == 'Scissors') or (users_input == 'scissors' and computer_input == 'Rock'):
                    users_score = users_score + 1
                    score_list = [x, users_score, computer_score]
                    score_table.append(score_list)
            else:
                    computer_score = computer_score + 1
                    score_list = [x, users_score, computer_score]
                    score_table.append(score_list)

            print(tabulate(score_table, headers=['Round','Users', 'Computers']))

        elif x == (no_round + 1):
            print('Thanks')
    return

if __name__ == '__main__':
    game()
