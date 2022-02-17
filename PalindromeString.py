def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    # a = int(input())
    # b = int(input())
    #
    # while a != 0:
    #     a, b = b % a, a
    # print("GDC is :",b)

    T = int(input())
    a = []
    def calculateHFC(a,b):
        while a != 0:
            a, b = b % a,a
        return b
    for i in range(T):
        a.append(list(map(int, input().split())))
    for i in range(len(a)):
        print(calculateHFC(a[i][0],a[i][1]))

if __name__ == '__main__':
    main()