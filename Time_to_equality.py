class Solution:
    # @param A : list of integers
    # @return an integer
    def BruteForce(self, A):
        n = len(A)
        for i in range(n):
            for j in range(n - 1):
                if A[j] > A[j + 1]:
                    A[j], A[j + 1] = A[j + 1], A[j]
        max = A[-1]
        count = 0
        for i in range(n):
            count = count + (max - A[i])
        return count
    def Optimized(self,A):
        n = len(A)
        max = A[0]
        for i in range(1,n):
            if A[i] > max:
                max = A[i]
        count = 0
        for i in range(n):
            count = count + (max - A[i])
        return count


s = Solution()
# print(s.BruteForce([2, 4, 1, 3, 2]))
# print(s.BruteForce([1,1,1,1]))
print(s.Optimized([2, 4, 1, 3, 2]))
print(s.Optimized([1,1,1,1]))