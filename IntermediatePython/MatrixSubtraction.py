class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        n = len(A)
        m = len(A[0])

        for i in range(n):
            # sub = 0
            for j in range(m):
                A[i][j] = A[i][j] - B[i][j]
        return A
s = Solution()
print(s.solve([[1, 2, 3],[4, 5, 6],[7, 8, 9]],[[9, 8, 7],[6, 5, 4],[3, 2, 1]]))
print(s.solve([[1, 1]],[[2, 3]]))