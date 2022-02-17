class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        n = A.find(B)
        if n == -1:
            return n
        return n + 1

s = Solution()
print(s.solve("lvnrqpz","rogq"))