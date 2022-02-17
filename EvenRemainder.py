def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    A = int(input())
    N = int(input())
    B = []
    flag = 0

    B = [int(i) for i in input().strip().split()[:N]]
    for j in range(N):
        even = B[j] % A
        if even % 2 == 0:
            flag += 1
    print(flag)
    return 0

if __name__ == '__main__':
    main()