# Given an integer,n, print the following values for each integer i from 1 to n:
#
# Decimal
# Octal
# Hexadecimal (capitalized)
# Binary


def print_formatted(number):
    if n in range(1, 100):
        for num_ in range(1, n+1):
            width = len("{0:b}".format(n))
            print('{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}'.format(num_, width=width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)