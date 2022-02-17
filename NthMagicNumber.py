class Solution:
    # @param A : integer
    # @return an integer
    def DecimalToBinary(self,A):
        return bin(A).replace("0b", "")
    def solve(self, A):
        n = int(self.DecimalToBinary(A))
        print(n)
        i = 0
        sum = 0
        while n > 0:
            i += 1
            rem = n % 10
            n = n // 10
            if rem == 1:
                sum = sum + 5 ** i
        return sum
s = Solution()
print(s.solve(10))
