class Solution:
    def maxArr(self,A):
        inf = 10 ** 9
        a = -inf
        b = inf
        c = -inf
        d = inf

        for i in range(len(A)):
            x = A[i]

            a = max(a,x + i)
            b = min(b,x + i)

            c = max(c,x - i)
            d = min(d,x - i)

        ans = max(a-b,c-d)
        return ans

s = Solution()
print(s.maxArr([1, 3, -1]))