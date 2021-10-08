# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
# Then print the respective minimum and maximum values as a single line of two space-separated long integers.


def miniMaxSum(arr):
    min_ = arr[0]
    max_ = arr[0]
    sum_ = 0
    for x in arr:
        sum_ += x

        if x > max_:
            max_ = x
        elif x < min_:
            min_ = x
    print(sum_ - max_, sum_ - min_)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)