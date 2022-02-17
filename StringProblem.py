class Solution:
    # @param A : string
    # @return a list of integers
    def solve(self, A):
        vcount = 0
        ccount = 0
        l = []
        vowel = ('a', 'e', 'i', 'o', 'u')

        for char in A:
            if char in vowel:
                vcount += 1
            else:
                ccount += 1
        l.append(vcount)
        l.append(ccount)
        return l
s = Solution()
print(s.solve('scaler'))

