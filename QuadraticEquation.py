def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    A = int(input())
    B = int(input())
    C = int(input())

    n = (B * B) - 4 * A * C
    if n > 0:
        print("1")
    elif n < 0:
        print("-1")
    else:
        print("0")

if __name__ == '__main__':
    main()