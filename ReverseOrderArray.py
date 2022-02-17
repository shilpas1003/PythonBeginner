class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        A.sort()
        print(A)

        #last element
        if A[len(A)-1]<= 0:
            return 1
        #checking 1 in the list or not
        isOne = False
        for i in range(0,len(A)):
            if A[i] == 1:
                isOne = True
        if isOne == False:
            return 1
        for i in range(0,len(A) - 1):
            if A[i] > 0 and (A[i+1] - A[i] > 1):
                return A[i] + 1
        return A[len(A)-1] + 1




s1 = Solution()
print(s1.firstMissingPositive([1,1,2,3,4,5,6]))
