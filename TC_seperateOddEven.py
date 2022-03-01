def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    T = int(input())
    a = []
    b = []
    even = []
    odd = []

    for i in range(0, T):
        b.append(int(input()))
        a.append(list(map(int, input().strip().split())))
    str = ' '
    for i in range(0,T):
        n = b[i]
        for j in range(0,n):
            if a[i][j] % 2 == 0:
                even.append(a[i][j])
            else:
                odd.append(a[i][j])
        # print(len(odd))
        # print(len(even))
        if len(odd) > 0:
            print(*odd, sep=' ',end=' \n')
            # print("\n")
        else:
            print('')
        if len(even) > 0:
            print(*even, sep=' ',end=' \n')
            # print("\n")
        else:
            print('')
        odd = []
        even = []

    return 0

if __name__ == '__main__':
    main()