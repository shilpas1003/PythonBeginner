class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def Brute_forcesolve(self, A, B):
        ans = -float('inf')
        n = len(A)

        for L in range(B):
            R = B - L

            left_sum = 0
            for i in range(L):
                left_sum += A[i]

            right_sum = 0
            for i in range(n-R,n):
                right_sum += A[i]

            total = left_sum + right_sum
            print(L, R, total)
            if total > ans:
                ans = total
        return ans

    def Optimized(self,A,B):
        answer = -float('inf')
        n = len(A)

        prefix = [0] * n
        prefix[0] = A[0]

        for i in range(1,n):
            prefix[i] = prefix[i-1] + A[i]

        for L in range(B):
            R = B - L
            if L == 0:
                left_sum = 0
            else:
                left_sum = prefix[L-1]

            if n-R-1 < 0 :
                right_sum = prefix[n-1]
            else:
                right_sum = prefix[n-1] - prefix[n-R-1]
            total = left_sum + right_sum
            if total > answer:
                answer = total
        return answer

    def carryforward(self,A,B):
        n = len(A)
        right_sum = 0
        left_sum = 0
        for L in range(B+1):
            R = B - L
            if R == 0:
                right_sum = 0
            else:
                right_sum = right_sum + A[n-R]
            if L == 0:
                left_sum = 0
            else:
                left_sum = left_sum + A[L-1]
            total = left_sum + right_sum
            print('Left Index :',L,'Right Index:', R,'Left Sum:',left_sum,'Right sum:',right_sum,'total :',total)

s = Solution()
# print("Brute Force : ",s.Brute_forcesolve([5, -2, 3 , 1, 2],3))
# print("Optimized : ",s.Optimized([5, -2, 3 , 1, 2],3))
print("carryforward : ",s.carryforward([5, -2, 3 , 1, 2],3))