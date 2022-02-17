class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        # sorted = True
        # print(A)
        # while sorted:
        #     sorted = False
        #     for i in range(len(A)-1):
        #         if A[i] > A[i+1]:
        #             A[i], A[i+1] = A[i+1], A[i]
        #             sorted = True
        # k = A[0]
        # for j in range(len(A)-1):
        #     k = A[j]



s1 = Solution()
s1.firstMissingPositive([3, 4, -1, 1])

