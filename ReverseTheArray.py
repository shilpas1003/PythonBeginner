class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def solve(self, A):
        B = list(A)
        i = 0
        j = len(B)-1

        while i <= j :
            t = A[i]
            B[i] = B[j]
            B[j] = t
            i += 1
            j -= 1
        return B

s = Solution()
print(s.solve([1,2,3,4,5]))