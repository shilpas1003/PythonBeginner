class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        #prefix sum : It will need extra space to store the value
        # p = [A[0]]
        # for x in A[1:]:
        #     p.append(x + p[-1])
        # n = len(A)
        # for i in range(n):
        #     left = p[i-1]
        #     right = p[n-1] - p[i]
        #     if left == right:
        #         return i
        # return -1

        #Cumulative sum : from left to right
        total = 0
        n = len(A)
        for x in A:
            total += x
        print(total)
        print(n)
        left = 0
        for i in range(n):
            right = total - left - A[i]
            if left == right:
                return i
            left += A[i]
        return -1

s = Solution()
print(s.solve([1,2,3,4,-1]))
