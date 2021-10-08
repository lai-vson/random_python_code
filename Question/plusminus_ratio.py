def plusMinus(arr):
    pos = 0
    neg = 0
    zer = 0
    arr = list(arr)
    for x in arr:
        if x > 0:
            pos += 1
        elif x < 0:
            neg += 1
        elif x == 0:
            zer += 1

    print('{:.6f}'.format(pos / len(arr)))
    print('{:.6f}'.format(neg / len(arr)))
    print('{:.6f}'.format(zer / len(arr)))


if __name__ == '__main__':
    n = int(input().strip())

    arr = map(int, input().rstrip().split())

    plusMinus(arr)

