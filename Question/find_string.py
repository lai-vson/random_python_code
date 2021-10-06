# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string.
# String traversal will take place from left to right, not from right to left.


def count_substring(string, sub_string):
    if len(string) in range(1, 201):
        # string = list(string)
        count = 0
        for x in range(len(string)):
            # print(string[x:x+3])
            if string[x:x+len(sub_string)] == sub_string:
                count += 1
            else:
                pass
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)
