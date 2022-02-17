def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    balance_in_bank = int(input())
    num_of_operation = int(input())
    list_opt = []
    for i in range(num_of_operation):
        list_opt.append(list(map(int,input().split())))

    for j in range(num_of_operation):
        # for k in range(0,2):
            if balance_in_bank < 0:
                print("Insufficient Funds")
            else:
                if list_opt[j][0] == 1:
                    balance_in_bank = balance_in_bank + list_opt[j][1]
                    print(balance_in_bank)
                elif list_opt[j][0] == 2:
                    balance_in_bank = balance_in_bank - list_opt[j][1]
                    if balance_in_bank < 0:
                        balance_in_bank = balance_in_bank + list_opt[j][1]
                        print("Insufficient Funds")
                    else:
                        print(balance_in_bank)
    return 0

if __name__ == '__main__':
    main()