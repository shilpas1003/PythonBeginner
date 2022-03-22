# You are given a 2D integer matrix A, return a 1D integer vector containing row-wise sums of original matrix.
class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A) #count of row
        m = len(A[0]) #count of col
        ans = []

        for i in range(n):
            sum = 0
            for j in range(m):
                sum += A[i][j]
            ans.append(sum)
        return ans

s = Solution()
print(s.solve([[1,2,3,4],
[5,6,7,8],
[9,2,3,4]]))