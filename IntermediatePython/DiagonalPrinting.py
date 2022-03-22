# print Diagonal indices
class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def print_rtl_diagonal(self, A):
        n = len(A)
        m = len(A[0])
        M =[[0] * m for _ in range(n)]
        print(M)
        for c in range(m):
            # print(c)
            r = 0
            while r < n and c >= 0:
                M[r][c] = A[r][c]
                # print(A[r][c])
                r += 1
                c -= 1
        # for r in range(1,n):
        #     c = m-1
        #     while r < n  and c >= 0:
        #         M[r][c] = A[r][c]
        #         r += 1
        #         c -= 1

        return M
    def print_ltr_diagonal(self,A):
        n = len(A)
        m = len(A[0])
        N = [[0] * m for _ in range(n)]
        # print(N)
        for r in range(n):
            c = 0
            while r < n and c >=0:
                N[r][c] = A[r][c]
                r += 1
                c += 1
        return N


s = Solution()
print('Right to Left :',s.print_rtl_diagonal([[1,2,3],[4,5,6],[7,8,9]]))
print('Left to Right :',s.print_ltr_diagonal([[1,2,3],[4,5,6],[7,8,9]]))