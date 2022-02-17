class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        f1 = 1
        f2 = 1
        if A == 1:
            return f1
        else:
            for i in range(2, A):
                f3 = f1 + f2
                f1 = f2
                f2 = f3
            return f3
s = Solution()
print(s.solve(1))