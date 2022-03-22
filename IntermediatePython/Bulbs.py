# Initial State of all bulbs
class Solution:
	# @param A : list of integers
	# @return an integer
	def bulbs(self, A):
		state = 0
		ans = 0

		for i in range(len(A)):
			if A[i] == state:
				ans += 1
				state = 1 - state
		return ans

s = Solution()
print(s.bulbs([0, 1, 0, 1]))
print(s.bulbs([1, 1, 1, 1]))