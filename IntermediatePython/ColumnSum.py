# You are given a 2D integer matrix A, return a 1D integer vector containing column-wise sums of original matrix.
class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A) #Number of Rows
        m = len(A[0]) #Number of Columns
        M = []

        for i in range(m):
            sum = 0
            for j in range(n):
                sum += A[j][i]
            M.append(sum)
        return M

s = Solution()
print(s.solve([[1,2,3,4],
[5,6,7,8],
[9,2,3,4]]))