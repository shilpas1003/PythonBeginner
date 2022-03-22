class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        n = len(A)
        count = 0
        # for s in range(len(A)):
        #     for e in range(s,n):
        #         ch = A[s:e+1]
        #         print(ch,ch[0])
        #         if (ch[0] == 'A' or ch[0] == 'a' or ch[0] == 'E' or ch[0] == 'e' or ch[0] == 'I'
        #                 or ch[0] == 'i' or ch[0] == 'O' or ch[0] == 'o' or ch[0] == 'U' or ch[0] == 'u'):
        #             count += n - i
        # return count % 10003

        n = len(A)
        count = 0
        for i in range(n):
            if (A[i] == 'A' or A[i] == 'a' or A[i] == 'E' or A[i] == 'e' or A[i] == 'I'
                    or A[i] == 'i' or A[i] == 'O' or A[i] == 'o' or A[i] == 'U' or A[i] == 'u'):
                count += (n - i)
        return count % 10003
s = Solution()
print(s.solve('ABEC'))
print(s.solve("pGpEusuCSWEaPOJmamlFAnIBgAJGtcJaMPFTLfUfkQKXeymydQsdWCTyEFjFgbSmknAmKYFHopWceEyCSumTyAFwhrLqQXbWnXSn"))
# print(s.solve('ABEC'))
# print(s.solve('ABEC'))