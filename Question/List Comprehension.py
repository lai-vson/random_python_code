# Print the list in lexicographic increasing order.

if __name__ == '__main__':
    list =[]
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    for i in range(0, x+1):
        for j in range(0, y+1):
            for k in range(0, z+1):
                if (i+j+k) != n:
                    list.append([i,j,k])
    print(list)
