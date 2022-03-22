class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        n = len(A) #NumOfRows
        m = len(A[0]) #NumOfColumn
        print(n)
        print(m)
        extraRow = [[0] * n]
        print(extraRow)
        extraCol = [[0] * m]
        print(extraCol)

        for i in range(n):
            for j in range(m):
                if A[i][j] == 0:
                    extraRow[0][i] = 1
                    extraCol[0][j] = 1
        print('rows:',extraRow)
        print('column:',extraCol)
        # print(A)
        #Converting row's values
        for i in range(n):
            if extraRow[0][i] == 1:
                for j in range(m):
                    A[i][j] = 0
        print('After Converting Rows ')
        print(A)
        #converting column's values
        for j in range(m):
            if extraCol[0][j] == 1:
                for i in range(n):
                    A[i][j] = 0
        print('After Converting Column ')
        print(A)
        # return A
s = Solution()
# print(s.solve([[1,2,3,4],[5,6,7,0],[9,2,0,4]]))
print(s.solve([[5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]]))