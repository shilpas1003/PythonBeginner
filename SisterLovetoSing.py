def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    str = input().split()
    A1 = int(str[0])
    A2 = int(str[1])
    B1 = int(str[2])
    B2 = int(str[3])
    l = []
    for i in range(A1,A2+1):
        for j in range(B1,B2+1):
            if i == j:
                l.append(i)
                break
    if len(l) > 1:
        print(max(l)-min(l))
    else:
        print("0")
if __name__ == '__main__':
    main()