class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        n,m = len(A),len(A[0])
        print('Row :',n)
        print('Column:',m)
        m_t = [[0] * n for _ in range(m)]
        print(m_t)
        for i in range(n):
            for j in range(m):
                m_t[j][i] = A[i][j]

        return m_t
s = Solution()
print(s.solve([[1, 2, 3],[4, 5, 6],[7, 8, 9]]))