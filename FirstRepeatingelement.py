import cryptography.hazmat.primitives.kdf.kbkdf


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        for i in range(len(A)):
            count = 0
            for j in range(len(A)):
                if A[i] == A[j]:
                    count += 1
                print(A[i], A[j],count)

s1 = Solution()
print(s1.solve([ 10, 5, 3, 4, 3, 5, 6 ]))
# s1.solve([ 10, 5, 3, 4, 3, 5, 6 ])
