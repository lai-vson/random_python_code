#check for the second runner up

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    list_ = sorted(list(arr))
    for x in list_:
        if x < max(list_):
            max_= x
    print(max_)