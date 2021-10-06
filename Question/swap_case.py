# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa

def swap_case(s):
    if len(s) in range(0, 1001):
        final_word = []
        for x in s:
            if x.islower() == True:
                x = x.upper()
            elif x.isupper() == True:
                x = x.lower()
            else:
                pass
            final_word.append(x)
        new_line = "".join(final_word)
    return new_line


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
