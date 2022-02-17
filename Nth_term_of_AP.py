class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        #t(n) = a  + (n-1)d
        a = A
        z = a + B
        d = z - a
        n = C
        term = a + (n-1) * d
        return term

s = Solution()
print(s.solve(1,1,5))