class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        # Also Special Subsequences "AG"
        count = 0
        gs = 0
        n = len(A)
        for i in reversed(range(n)):
            if A[i] == 'G':
                gs += 1
            elif A[i] =='A':
                count += gs
        return count

s = Solution()
print(s.solve("ABCGAG"))
