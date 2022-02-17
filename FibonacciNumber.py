# def main():
#     # YOUR CODE GOES HERE
#     # Please take input and print output to standard input/output (stdin/stdout)
#     # E.g. 'input()/raw_input()' for input & 'print' for output
#     A = int(input())
#     f1 = 0
#     f2 = 1
#     m = 10 ** 9 + 7
#     for i in range(2,A+1):
#         f3 = (f1 + f2) % m
#         f1,f2 = f2,f3
#     print(f3)
#     return 0
#
# if __name__ == '__main__':
#     main()

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        f1 = 0
        f2 = 1
        m = 10 ** 9 + 7
        for i in range(2,A+1):
            f3 = (f1 + f2) % m
            f1,f2 = f2,f3
        return f3

s = Solution()
print(s.solve(3))