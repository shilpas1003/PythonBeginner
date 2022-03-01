class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        # print(n)
        if n > 1:
            for i in range(0,n-1):
                flag = 0
                for j in range(0,n-1-i):
                    if A[j] > A[j+1]:
                        temp = A[j]
                        A[j] = A[j+1]
                        A[j+1] = temp
                        flag = 1
                if flag != 1:
                    break;
            return A[-2]
        else:
            return -1
s = Solution()
print(s.solve([2]))
