class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        # c = []
        # for i in range(len(B)):
        #     count = 0
        #     n = B[i] #20
        #     for j in range(len(A)):
        #             if n > A[j]:
        #                 n = n - A[j]
        #                 count += 1
        #  c.append(count)
        # return
        #
        # # for i in range(len(B)):
        # #     target = B[i]
        # #     start = 0
        # #     end = len(A) - 1
        # #     count = 0
        # #     while start <= end:
        # #         mid = (start + end) // 2
        # #         if A[mid] == target:
        # #             count += 1
        # #             break
        # #         elif A[mid] > target:
        # #             end = mid - 1
        # #         elif A[mid] < target:
        # #             start = mid + 1
        # #     if count > 0:
        # #         c.append(count)
        # #
        # #     else:
        # #         count = len(A)
        # #         c.append(count)
        # # return c
        for i in range(1,len(A)):
            A[i]= A[i] + A[i-1]
        print(A)

        for j in range(1,range(B)):



s = Solution()
print(s.solve([3,4,4,6],[20,4,10,2]))
# print(s.solve([ 23, 36, 58, 59 ],[ 3, 207, 62, 654, 939, 680, 760 ]))

