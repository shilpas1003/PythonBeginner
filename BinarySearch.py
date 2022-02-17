def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    a = [1,5,7,10,15,20,23]
    target = 7
    n = len(a)
    start = 0
    end = n-1
    ans = -1

    while start<=end:
        mid = (start + end) // 2
     #case 1 : found Target Number
        if a[mid] == target:
            ans = mid
            break
     #case 2 : Mid number is greater than target then search in left part
        elif a[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    print(ans)
if __name__ == '__main__':
    main()