def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    a = list(map(int, input().split()))
    b = [x for x in a if x < 0]

    for i in range(len(b)):
        print(b[i], end=' ')

if __name__ == '__main__':
    main()