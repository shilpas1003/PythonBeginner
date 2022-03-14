class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        prod = []
        n = len(A)
        for i in range(n):
            product = 1
            for j in range(n):
                if i == j:
                    continue
                else:
                    product = product * A[j]
            prod.append(product)
        return prod

s = Solution()
print(s.solve([1, 2, 3, 4, 5]))
print(s.solve([5, 1, 10, 1]))
