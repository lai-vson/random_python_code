# You are given a string  and width .
# Your task is to wrap the string into a paragraph of width .

import textwrap

def wrap(string, max_width):
    result = textwrap.wrap(string,width=max_width)
    return '\n'.join(result)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)