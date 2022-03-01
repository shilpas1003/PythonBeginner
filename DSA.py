def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    def solve(N):
        for i in range(2 ** N):
            j = i
            print("value of i : ",i)
            while j > 0:
                print("value of j : ", j)
                j -= 1


    solve(4)

if __name__ == '__main__':
    main()