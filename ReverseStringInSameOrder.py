def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    sentence = input()
    n = len(sentence.split())
    for word in sentence.split():
        str = word[::-1]
        if n == 1:
            print(str)
        else:
            print(str,end=' ')
        n -= 1
    return 0

if __name__ == '__main__':
    main()