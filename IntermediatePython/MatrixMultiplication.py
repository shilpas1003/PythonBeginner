class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        n = len(A) #rows count for A
        m = len(B[0]) #column count for B
        mul = [[0] * m for _ in range(n)]
        print(mul)
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    mul[i][j] += A[i][k] * B[k][j]

        return mul

s = Solution()
print(s.solve([[1,2],[3,4]],[[5,6],[7,8]]))
print(s.solve([[94,91]],[[35, -52, -12, 26, -93, -61],[29, -20, -36, -9, 66, 15]]))