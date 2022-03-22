class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        # n = len(A)
        # B = [[0] * n]
        # print(B)
        ans = 0
        for i in range(len(A)):
            ans ^= A[i]
        return ans


s = Solution()
print(s.singleNumber([8,18,8]))