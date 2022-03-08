class Solution:
    # @param A : list of integers
    # @return an integer
    def Bruteforce(self, A):
        count = 0
        n = len(A)
        for i in range(n):
            leader = True
            for j in range(i+1,n):
                if A[i] <= A[j]:
                    leader = False
                    break
            if leader:
                count += 1
        return count

    def Optimized(self, A):
        n = len(A)
        max = [0] * n
        var_max = A[n-1]
        max[n-1] = var_max
        print(max)
        for i in reversed(range(n)):
            if A[i] > var_max:
                var_max = A[i]
                max[i] = var_max
            else:
                max[i] = var_max
        print(max)
        count = 0
        for i in range(n):
            leader = True
            if A[i] > max[i]:
                leader = False
                break
        if leader:
            count += 1
        return count

    # def carryForward(self,A):
s = Solution()
print("Brute force: ",s.Bruteforce([1,7,8,-6,0,3,-7,-10]))
print("Optimized: ",s.Optimized([1,7,8,-6,0,3,-7,-10]))
# print('BruteForce Method Answer : ',s.Bruteforce('abrgxabggxag'))
# print('Time Complexity Method Answer : ',s.Optimized('abrgxabggxag'))
# print('Carry Forward : ',s.carryForward('abrgxabggxag'))