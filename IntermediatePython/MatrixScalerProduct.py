class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return a list of list of integers
    def solve(self, A, B):
        n = len(A)
        m = len(A[0])

        for i in range(n):
            for j in range(m):
                A[i][j] = A[i][j] * B

        return A
s = Solution()
print(s.solve([[1, 2, 3],[4, 5, 6],[7, 8, 9]],2))