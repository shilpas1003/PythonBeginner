class Solution:
    # @param A : list of integers
    # @return an integer
    def Bruteforce(self, A):
        #bruteForce Method
        n =len(A)
        c = 0
        for i in range(n):
            for j in range(i+1,n):
                if A[i] == 'a' and A[j] == 'g':
                  c += 1
        return c

    def Optimized(self, A):
        n = len(A)
        g_count = [0] * n
        count = 0
        for i in reversed(range(n)):
            if A[i] == 'g':
                count += 1
            g_count[i] = count
        print("Postfix :",g_count)
        count = 0
        for i in range(n):
            if A[i] == 'a':
                count += g_count[i]
        return count
        ## Time Complexity = O(N)
        ## Space Complexity = O(N)
    def carryForward(self,A):
        n = len(A)
        count = 0
        gs = 0
        for i in reversed(range(n)):
            if A[i] == 'a':
                count += gs
            elif A[i] == 'g':
                gs += 1
        return count


s = Solution()
# print(s.solve([a,b,r,g,x,a,b,g,g,x,a,g]))
print('BruteForce Method Answer : ',s.Bruteforce('abrgxabggxag'))
print('Time Complexity Method Answer : ',s.Optimized('abrgxabggxag'))
print('Carry Forward : ',s.carryForward('abrgxabggxag'))