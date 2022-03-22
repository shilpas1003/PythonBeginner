class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        result = 0
        for i in range(32):
            result = result << 1

            if A & 1 == 1:
                result += 1
            A = A >> 1
        return result

s = Solution()
print(s.reverse(3))
print(bin(11).replace('0b',''))