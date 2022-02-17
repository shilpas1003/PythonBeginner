class Solution:
    # @param A :string
    # @return an integer
    def solve(self,A):
        #declare a frequency map(dictonary)
        freq = {}
        for char in A:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        # Freq map create

        odd_frequencies = 0
        for frequency in freq.values():
            if frequency % 2 == 1:
                odd_frequencies += 1

        if odd_frequencies <= 1:
            return 1
        else:
            return 0

s1 = Solution()
print(s1.solve('abcde'))