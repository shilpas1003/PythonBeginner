class Solution:
    # @param A : list of integers
    # @return an integer
    def practice(self, A):
        print(A)
        n = len(A)
        m = len(A[0])
        print(n,m)

        for irow in range(n):
            for icol in range(m):
                print(A[irow][icol],end=' ')
            print()
        print('2nd Method')
        for row in A:
            for element in row:
                print(element, end=' ')
            print()

    def Print_Matrix(self,M):
        for row in M:
            print(row)
    def Empty_Grow(self,A,B):
        # 2nd method:
        n = A
        m = B
        S = []
        for i in range(n):
            S.append([])
            for j in range(m):
                v = (j + 1) ** (i + 1)
                S[i].append(v)
        self.Print_Matrix(S)
        # return S
    def full_sized_overwrite(self,A,B):
        M = [[0] * B for _ in range(A)]
        self.Print_Matrix(M)
        print('_' * 100)
        for i in range(A):
            for j in range(B):
                val = (j+1) ** (i+1)
                M[i][j] = val
                self.Print_Matrix(M)
                print('_' * 100)
s = Solution()
# M = [[s + i * i for i in range(5)] for s in range(0,50,10)]
# s.practice(M)
# print(s.Empty_Grow(4,8))
print('_'*100)
print(s.full_sized_overwrite(4,8))

