class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        # n = len(A)
        # m = len(A[0])
        # mm = (2 * n) - 1
        # M = [[0]*n for _ in range(mm)]
        # print(M)
        # for i in range(m+n-1):
        #     for j in range(m):
        #         for k in range(n):
        #             if j + k == i:
        #                 print(A[j][k],end=" ")
        #     print()
        #
        # for i in range((i+1)%3):
        #     for j in reversed(range(m,0))
        # # return M
        p = len(A[0])
        res = [0] * (2 * p - 1)
        print(p)
        print(res)
        for i in range((2 * p) - 1):
            res[i] = []
        print(res)
        for i in range(p):
            for j in range(p):
                res[i + j].append(A[i][j])
        print(res)
        for i in range(2 * p - 1):
            while len(res[i]) < p:
                res[i].append(0)
        return res

s = Solution()
print(s.diagonal([[1,2,3],
[4,5,6],
[7,8,9]]))