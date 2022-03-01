class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        for i in range(0, len(A)):
            for j in range(i+1, len(A)):
                if i != j:
                    sum = A[i] + A[j]
                    if sum == B:
                        return 1
        return 0

s = Solution()
print(s.solve([510827, 351151, 96897, 925335, 299818, 192489, 456948, 44720, 510589, 598577],808099))
print(s.solve([ 1, 2, 4 ],4))