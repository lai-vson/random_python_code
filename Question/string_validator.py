# You are given a string .
# Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.


if __name__ == '__main__':
    s = input()
    s = list(s)

    if len(s) in range(0, 1001):
        print(any(x.isalnum() for x in s))
        print(any(x.isalpha() for x in s))
        print(any(x.isdigit() for x in s))
        print(any(x.islower() for x in s))
        print(any(x.isupper() for x in s))
