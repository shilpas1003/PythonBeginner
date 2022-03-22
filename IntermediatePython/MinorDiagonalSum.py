class Solution:
    # @param A : tuple of list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        m = len(A[0])
        sum = 0
        # for i in range(n):
        #     for j in range(m):
        #         if i + j == n-1 :
        #             sum += A[i][j]
        # return sum
        print('Main Diagonal Sum :')
        for i in range(n):
            for j in range(m):
                if i == j:
                    sum += A[i][j]
        return sum
s = Solution()
print(s.solve([[1, -2, -3],
      [-4, 5, -6],
      [-7, -8, 9]]))
print(s.solve([[3, 2],
      [2, 3]]))