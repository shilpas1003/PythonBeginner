# You are given two matrices A & B of same size, you have to return another matrix which is the sum of A and B.
class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        n_A = len(A)  # row from matrix A
        m_B = len(B[0])  # column from Matrix B
        for i in range(n_A):
            for j in range(m_B):
                A[i][j] = A[i][j] + B[i][j]
        return A
s = Solution()
print(s.solve(
    [
      [6],
      [2],
      [3],
      [10],
      [1],
      [3]
    ],
    [
      [6],
      [7],
      [3],
      [8],
      [1],
      [2]
    ]
))





