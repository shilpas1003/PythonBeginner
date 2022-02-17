class Solution:
    def twoSum(self,A,B):
            num_to_index = {}

            for i in range(len(A)):
                req = B - A[i]

                if req in num_to_index:
                    return num_to_index[req] + 1 , i + 1
                    # print(num_to_index[req] + 1 , i + 1)

                if A[i] not in num_to_index:
                    num_to_index[A[i]] = i
            return []

s = Solution()
print(s.twoSum([2,7,11,15],9))