def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    T = int(input())
    a = []
    b = []

    for i in range(0,T):
        a.append(list(map(int,input().split())))
        b.append(int(input()))

    # for i in range(0,len(a)):
    #         print('A[',i,'] :',a[i])
    # for i in range(0,len(b)):
    #         print('B[',i,'] :',b[i])

    # print(len(a[0]))
    for i in range(0,T):
        flag = 0
        for j in range(1,len(a[i])):
            if b[i] == a[i][j]:
                flag += 1
                break
        if flag > 0:
            print('1')
        else:
            print('0')
if __name__ == '__main__':
    main()