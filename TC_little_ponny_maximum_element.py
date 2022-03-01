class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        count = 0
        for i in range (n):
            if B < A[i]:
                count = count + 1

        return count
        # for i in range(0,n):
        #     flag = 0
        #     for j in range(0,n-1-i):
        #         if A[j] > A[j+1]:
        #             temp = A[j]
        #             A[j] = A[j+1]
        #             A[j+1] = temp
        ans = 0
        # for i in range(0,n):
        #     if A[i] == B:
        #         ans = (len(A)-1) - i
        # if ans > 0:
        #     return ans
        # else:
        #     return -
        # print(A)
        # start = 0
        # end = n - 1
        # ans = -1
        # while start <= end:
        #     mid = (start + end) // 2
        #     if A[mid] == B:
        #         ans = mid
        #         # break
        #         start = mid + 1
        #     elif A[mid] > B:
        #         end = mid - 1
        #     else:
        #         start = mid + 1
        # print('index : ',ans)
        # if ans > 0:
        #     return len(A) - 1 - ans
        # else:
        #     return -1

s = Solution()
print(s.solve([3,1,2,2,4,1],3))