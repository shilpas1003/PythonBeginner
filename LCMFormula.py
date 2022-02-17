class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def hcf(self,A, B):
        while (A != 0):
            A, B = B % A, A
        return B
    def solve(self, A, B):
        n = self.hcf(A, B)
        lcm = (A * B) // n
        return lcm
s = Solution()
print(s.solve(2,3))
print(s.solve(9,6))
print(s.solve(2,6))