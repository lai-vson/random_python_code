# You are given an integer, n. Your task is to print an alphabet rangoli of size . (Rangoli is a form of Indian folk art based on creation of patterns.)

import string
alpha = string.ascii_lowercase

def print_rangoli(size):
    L = []
    for i in range(n):
        s = "-".join(alpha[i:n])
        L.append((s[::-1] + s[1:]).center(4 * n - 3, "-"))
    print('\n'.join(L[:0:-1] + L))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)