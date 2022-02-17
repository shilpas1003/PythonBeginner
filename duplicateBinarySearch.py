def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    a = [1,2,2,2,2,3,3,3,3,4,4]
    target = 2
    n = len(a)
    start = 0
    end = n-1
    ans = -1

    while start<=end:
        mid = (start + end) // 2
        if a[mid] == target:
            ans = mid
            # break
            end = mid - 1
        elif a[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    print(ans)
if __name__ == '__main__':
    main()