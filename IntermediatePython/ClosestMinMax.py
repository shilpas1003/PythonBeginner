class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        minVal = min(A)
        maxVal = max(A)

        iMin = -1
        iMax = -1
        min_length = len(A)

        for i in range(len(A)):
            if A[i] == minVal:
                iMin = i
                if iMax != -1:
                    length = iMin - iMax + 1
                    min_length = min(length,min_length)
            if A[i] == maxVal:
                iMax = i
                if iMin != -1:
                    length = iMax - iMin + 1
                    min_length = min(length,min_length)
        return min_length

s = Solution()
# 4
print(s.solve([2,-1,6,8,-1,3,0,8,0,8,2,-1]))