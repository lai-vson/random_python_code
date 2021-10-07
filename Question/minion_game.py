# Your task is to determine the winner of the game and their score


def minion_game(string):
    play1 = 0
    play2 = 0
    vowels = 'AEIOU'
    for i in range(len(string)):
        if string[i] in vowels:
            play1 += len(string) - i
        else:
            play2 += len(string) - i

    if play1 > play2:
        print('Kevin', play1)
    elif play2 > play1:
        print('Stuart', play2)
    elif play1 == play2:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)

