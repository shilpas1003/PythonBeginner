def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    n = list(map(int,input().split()))
    max = n[1]
    min = n[1]
    for i in range(2,len(n)):
        #maximum input
        if n[i] > max:
            max = n[i]
        #minimum element
        if n[i] < min:
            min = n[i]
    print(max,' ',min)
    return 0


if __name__ == '__main__':
    main()