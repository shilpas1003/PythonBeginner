class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
     # @return an list of long
    def BruteForce_rangeSum(self, A, B):
        n = len(B)
        # print(n)
        ans = []

        for i in range(n):
            start = B[i][0]
            end = B[i][1]
            # print('start : ',start,'end :',end,'i :',i)
            sum = 0
            for j in range(start-1,end):
                sum += A[j]
            ans.append(sum)

        return ans

    def Optimized(self, A, B):
      # Step 1 : Prefix sum of array A
        ans = []
        p = [A[0]]
        for x in A[1:]:
            p.append(p[-1] + x)
        n = len(B)
        for i in range(n):
            start = B[i][0] - 1
            end = B[i][1] - 1
            if start == 0:
                sum = p[end]
            else:
                sum = p[end] - p[start - 1]
            ans.append(sum)
        return ans

s = Solution()
# print(s.BruteForce_rangeSum([1, 2, 3, 4, 5],[[1, 4], [2, 3]]))
# print(s.BruteForce_rangeSum([2, 2, 2],[[1, 1], [2, 3]]))
print('2nd Example')
print(s.Optimized([1, 2, 3, 4, 5],[[1, 4], [2, 3]]))
print(s.Optimized([2, 2, 2],[[1, 1], [2, 3]]))