class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        # count number of Odd numbers element
        count = 0
        for i in range(len(A)):
            if A[i] % 2 != 0:
                count += 1

        if count % 2 != 0:
            return 'No'
        else:
            return 'Yes'
s = Solution()
print(s.solve([8]))