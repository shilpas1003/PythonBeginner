class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        binNum = bin(A).replace("0b","")
        # print(binNum)
        n = len(binNum)
        # print(n)
        flag = 0
        for i in range(1,n+1):
          if A & (1 << (i-1)) != 0:
              flag += 1
        return flag

s = Solution()
print(s.numSetBits(11))