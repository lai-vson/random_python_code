# Given an array of integers, where all elements but one occur twice, find the unique element.

def lonelyinteger(a):
    if n in range(1, 101) and len(a) in range(1, 101):
        b = {}
        for x in a:
            if x not in b:
                b[x] = 1
            else:
                b[x] += 1
        for k, v in b.items():
            if v == 1:
                final = k
    return final

if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    print(lonelyinteger(a))