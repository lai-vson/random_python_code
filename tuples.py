# Given an integer, n, and n space-separated integers as input, create a tuple, t, nof those  integers. Then compute and print the result of hash(t).


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split(" "))

    print(hash(tuple(integer_list)))