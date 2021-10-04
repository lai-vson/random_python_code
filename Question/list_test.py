# Consider a list (list = []). You can perform the following commands:
#
# insert i e: Insert integer e at position i.
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list

if __name__ == '__main__':
    list = []
    N = int(input())

    for i in range(N):
        cmd = input()
        if cmd.split()[0] == 'insert':
            list.insert(int(cmd.split()[1]), int(cmd.split()[2]))
        elif cmd.split()[0] == 'append':
            list.append(int(cmd.split()[1]))
        elif cmd.split()[0] == 'remove':
            list.remove(int(cmd.split()[1]))
        elif cmd.split()[0] == 'sort':
            list.sort()
        elif cmd.split()[0] == 'pop':
            list.pop()
        elif cmd.split()[0] == 'reverse':
            list.reverse()
        elif cmd.split()[0] == 'print':
            print(list, end='\n')


