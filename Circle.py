import math
# class Solution:
#     # @param A : integer
#     # @return an integer
#     def solve(self, A):
#        #Volume of a sphere having radius R is given by (4 * π * R3) / 3
#         n = math.pi
#         sq_r = A ** 3
#         volume_sphere = (4 * n * sq_r) / 3
#         print(math.ceil(volume_sphere))
# #
# # s = Solution()
# # s.solve(4)
# class Solution:
#     # @param A : integer
#     # @return an integer
#     def solve(self, A):
#         n = math.pi
#         sq_r = A ** 2
#         area_circle = n * sq_r
#         return math.ceil(area_circle)
#
# s = Solution()
#

# #### Factorial of a Number
# class Solution:
#     # @param A : integer
#     # @return an integer
#     def solve(self, A):
#         fact = 1
#         for i in range(1,A+1):
#             fact *= i
#         return fact
#
# s = Solution()
# print(s.solve(1))

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
      if A == 2:
          if B % 400 == 0 or (B % 100 != 0 and B % 4 == 0):
              return 29
          else:
              return 28
      elif A == 4 or A == 6 or A == 9 or A == 11:
          return 30
      else:
          return 31

s = Solution()
print(s.solve(2,9100))