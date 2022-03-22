class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        # O_row = len(A)
        # O_col = len(A[0])
        # F_row = (2 * O_row) - 1
        # print('Column :' ,O_row)
        # print('Row :',F_row)
        # Final_Mat = [[0] * O_row for _ in range(F_row)]
        # print(Final_Mat)
        #
        # for c in range(O_col):
        #     r = 0
        #     while r < O_row and c >= 0:
        #         print(A[r][c],r,c)
        #         r += 1
        #         c -= 1
        #
        #     print('brk')
        # return Final_Mat
        p = len(A[0])
        print(p)
        res = [0] * (2 * p - 1)
        # print(res)
        for i in range((2 * p) - 1):
            res[i] = []
        print(res)
        for i in range(p):
            for j in range(p):
                res[i + j].append(A[i][j])
        for i in range(2 * p - 1):
            while len(res[i]) < p:
                res[i].append(0)
        return res


s = Solution()
print(s.diagonal([[1,2,3],
[4,5,6],
[7,8,9]]))

# s.diagonal([[1,2],
# [4,5]])