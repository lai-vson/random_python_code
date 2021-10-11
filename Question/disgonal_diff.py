# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

def diagonalDifference(arr):
    n, t1, t2 = 0, 0, 0
    y = len(arr[0])
    for x in arr:
        t1 += x[n]
        n += 1
        # print(t1)

    for z in arr:
        t2 += z[y-1]
        y -= 1
        # print(t2)

    final = abs(t1 - t2)
    print(final)

if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
