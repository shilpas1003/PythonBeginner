class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A):
        # Method 1 :
        # prefix_sum = []
        # sum = 0
        # for i in range(len(A)):
        #     sum += A[i]
        #     prefix_sum.append(sum)
        # return prefix_sum
        prefix_sum = [A[0]]
        for i in range(1,len(A)):
            prefix_sum.append(A[i] + prefix_sum[-1])
        return prefix_sum

s = Solution()
print(s.solve([3,1,2,2,4,1]))