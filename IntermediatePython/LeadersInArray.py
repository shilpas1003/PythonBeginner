class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        max = A[-1]
        max_ele = []
        n = len(A)
        max_ele.append(max)
        for i in reversed(range(n)):
            if A[i] > max:
                max = A[i]
                max_ele.append(max)
        return max_ele
s = Solution()
print(s.solve([16, 17, 4, 3, 5, 2]))
print(s.solve([1,2]))