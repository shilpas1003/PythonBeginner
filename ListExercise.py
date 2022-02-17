class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def linearSearch(self, A, B):
        flag = 0
        for i in range(1,len(A)):

            if B == A[i]:
                flag = 1
                break
            else:
                flag = 0

        if flag == 1:
            return 1
        else:
            return 0

s1 = Solution()
print(s1.linearSearch([1, 4, 3, 2],5))

