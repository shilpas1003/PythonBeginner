class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        odd = []
        even = []
        n = len(A)
        odd = [0] * n
        print(odd)
        even = [0] * n
        print(even)

        #o will be come under even,hence even[0] will update
        even[0] = A[0]
        print(even)
        for i in range(1,n):
            odd[i] = odd[i-1]
            even[i] = even[i-1]

            if i % 2 == 0:
                even[i] = A[i] + even[i-1]
            else:
                odd[i] = A[i] + odd[i-1]
        print("Prefix Odd :",odd)
        print("Prefix Even : ",even)
        flag = 0
        p = odd[n-1]
        q = even[n-1] - A[0]
        print("P :",p)
        print("q : ",q)

s = Solution()
print(s.solve([2, 1, 6, 4]))