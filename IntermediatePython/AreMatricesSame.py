class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        #number of rows
        n = len(A)
        #number of columns
        m = len(A[0])
        flag = 1
        for i in range(n):
            for j in range(m):
                if A[i][j] != B[i][j]:
                    flag = 0
                    break

        if flag == 0:
            return 0
        else:
            return 1

s = Solution()
print(s.solve([[1, 2, 3],[4, 5, 6],[7, 8, 9]],[[1, 2, 3],[4, 5, 6],[7, 8, 9]]))
print(s.solve([[1, 2, 3],[4, 5, 6],[7, 8, 9]],[[1, 2, 3],[7, 8, 9],[4, 5, 6]]))

