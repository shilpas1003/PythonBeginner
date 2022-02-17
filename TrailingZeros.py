import math
class Solution:
	# @param A : integer
	# @return an integer
	def trailingZeroes(self, A):
		result = 0
		den = 5

		x = A // den
		while x >= 1:
			result += x
			den *= 5
			x = A // den
		return result

s = Solution()
print(s.trailingZeroes(50))
print(math.factorial(50))