import math
class Solution:
    def solve(self,A):
        even = []
        odd = []
        for i in range(len(A)):
            if A[i] % 2 == 0:
                even.append(A[i])
            else:
                odd.append(A[i])

        max_of_A = max(even)
        min_of_A = min(odd)

        return max_of_A - min_of_A

s = Solution()
print(s.solve([5,17,100,1]))