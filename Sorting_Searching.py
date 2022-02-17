# def main():
#     # YOUR CODE GOES HERE
#     # Please take input and print output to standard input/output (stdin/stdout)
#     # E.g. 'input()/raw_input()' for input & 'print' for output
#     def sorting(A):
#         for i in range(len(A)):
#             for j in range(len(A)-1):
#                 #pick two consecutive element
#                 # If they are not in correct order, swap them
#                 if A[j] > A[j+1]:
#                     A[j],A[j+1] = A[j+1],A[j]
#         return A
#     list = [ 627, 619, 852, 472, 858, 994, 323, 738, 177, 625, 946, 730, 832, 12, 526, 361, 343, 782, 289 ]
#     print(sorting(list))
# if __name__ == '__main__':
#     main()

class Solution:

    def bubbleSort(self,A):
        for i in range(len(A)):
            count = 0
            for j in range(len(A)-1):
                count = count + 1
                if A[j] > A[j+1]:
                    A[j],A[j+1] = A[j+1],A[j]
        return A,count

s = Solution()
print(s.bubbleSort([6,7,9,8]))