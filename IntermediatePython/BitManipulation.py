class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def to_binary(self, A):
        ans = " "
        while A > 0:
            remainder = A % 2
            ans += str(remainder)
            A = A // 2

        return ans[::-1]


s = Solution()
print(s.to_binary(78))