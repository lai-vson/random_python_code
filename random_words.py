def check():
    testword_list = []
    guessword_list = []
    n = 0

    test_word = input('Kindly input test words: ')
    while test_word.isalpha() != True:
        test_word = input('Please key in ONLY alphabet: ')

    guess_word = input('What word do you guess?: ')
    while guess_word.isalpha() != True:
        guess_word = input('Please key in ONLY alphabet: ')

    for list_test_word in test_word:
        testword_list.append(list_test_word)

    for list_guess_word in guess_word:
        guessword_list.append(list_guess_word)

    for y in guessword_list:
        if y in testword_list :
            n = n + 1
            testword_list.remove(y)
    return print('There are {} same characters.'.format(n))

if __name__ == '__main__':
    check()
