def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    a = [4,2,5,6,12,7,1,-1]
    key = 12
    ans = -1
    for i in range(len(a)):
        if a[i] == key:
            ans = i
            break

    if ans == -1:
        print("Not found")
    else:
        print("Found at index",ans)
if __name__ == '__main__':
    main()