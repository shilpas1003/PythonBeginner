class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, B):
        num_to_index = {}
        for i in range(len(A)):
            required_num = B - A[i]

            if required_num in num_to_index:
                return num_to_index[required_num]+1,i+1

            if A[i] not in num_to_index:
                num_to_index[A[i]] = i
        return []

s1 = Solution()
print(s1.twoSum([2,2,7,11,15],13))