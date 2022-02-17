class Solution:
    def solve(self,A,B):
        max = []

        for i in range(len(A)):
            if A[i] > B:
                max.append(A[i])

        if B in A:
            return len(max)
        else:
            return -1

        # print(len(max))

s = Solution()
print(s.solve([24,33,13,11,30,28,19,8,30,25,42,6,30,49,24,13,3,50],13))