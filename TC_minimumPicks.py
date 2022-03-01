class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        even = []
        odd = []
        for i in range(0,n):
            if A[i] % 2 == 0:
                even.append(A[i])
            else:
                odd.append(A[i])
        max = even[0]
        min = odd[0]
        for i in range(1,len(even)):
            if even[i] > max:
                max = even[i]
        for j in range(1,len(odd)):
            if odd[j] < min:
                min = odd[j]
        return max - min
s = Solution()
print(s.solve([5, 17, 100, 1]))