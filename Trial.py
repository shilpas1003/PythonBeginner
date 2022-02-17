# def main():
#     in_list = list(map(int,input().split()))
#     print(in_list)
#
#     return 0
#
# if __name__ = '__main__':
#     main()

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    # in_list = list(map(int, input().split()))
    in_list = input().split()
    A1 = in_list[0]
    A2 = in_list[1]
    B1 = in_list[2]
    B2 = in_list[3]
    print(A1)
    print(A2)
    print(B1)
    print(B2)
    str = int(A1)
    for i in range(int(A2)):
        " ".join(str,i)
    # # print("Ananya List")
    # # Ananya = []
    # for i in range(A1,A2+1):
    #     # Ananya.append(i)
    #     var1 = A1
    # print(Ananya)
    # print("Bhavya List")
    # Bhavya = []
    # for i in range(B1, B2 + 1):
    #     Bhavya.append(i)
    # print(Bhavya)
    #
    # common_fac = [i for i in Ananya if i in Bhavya]
    # print(common_fac)
    #
    # if len(common_fac) > 1:
    #     print(max(common_fac) - min(common_fac))
    # else:
    #     print("0")


if __name__ == '__main__':
    main()