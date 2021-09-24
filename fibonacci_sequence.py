fs_list = [0, 1]
fs_ = 0
user_input = int(input('Please enter a number to check if in fibonacci squence.\n: '))

def check():
    global fs_list, fs_, n
    while True:
        fs_ = fs_list[0] + fs_list[1]
        if fs_ == user_input:
            print('Yes, is in fibonacci sequence')
            quit()
        elif fs_ < user_input:
            fs_list[0] = fs_list[1]
            fs_list[1] = fs_
            # print(fs_list)
        elif fs_ > user_input:
            print('Not in fibonacci sequence')
            quit()


if __name__ == '__main__':
    check()
