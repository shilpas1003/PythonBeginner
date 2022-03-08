class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        odd_presum = [0] * (n+1)
        even_presum = [0] * (n+1)
        # print('Odd sum :',odd_presum)
        # print('Even sum :', even_presum)

        #calculation presum

        for i in range(n):
            if i % 2:
                odd_presum[i+1] = odd_presum[i] + A[i]
                even_presum[i+1] = even_presum[i]
            else:
                even_presum[i+1] = even_presum[i] + A[i]
                odd_presum[i+1] = odd_presum[i]
        # print('After calculating Presum :')
        # print('Odd sum :', odd_presum)
        # print('Even sum :', even_presum)
        # print(odd_presum[-1])
        # print(even_presum[-1])
        ans = 0
        for i in range(1,n+1):
            osum1 = odd_presum[i-1]
            esum1 = even_presum[i-1]

            osum2 = even_presum[-1] - even_presum[i]
            esum2 = odd_presum[-1] - odd_presum[i]

            if osum1 + osum2 == esum1 + esum2:
                ans += 1
        return ans

s = Solution()
print(s.solve([2, 1, 6, 4]))
print(s.solve([1, 1, 1]))