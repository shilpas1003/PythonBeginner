def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    # A = list(map(int, input().split()))
    # Method 1
    # A = [4,1,2,3,4]
    # D = []
    # c = 20
    # n = len(A)
    # c = c % (n -1)
    # for i in range(n-c, n):
    #     print(A[i],end=' ')
    #
    # for i in range(1, n  - c):
    #     print(A[i],end=' ')

   # Method 2
    A = [4,1,2,3,4]
    B = 2
    temp = []
    for i in range(B,len(A)):
        temp.append(A[i])
    i = 0
    for i in range(1,2):
        temp.append(A[i])
    A = temp.copy()
    print(A)
if __name__ == '__main__':
    main()