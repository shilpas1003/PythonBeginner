class Solution:
	# @param A : string
	# @param B : string
	# @return a strings
	def addBinary(self, A, B):
		Alen = len(A)
		Blen = len(B)
		print('L of A:',Alen)
		print('L of B:',Blen)
		# Step 1 : padding with zero
		if Alen > Blen:
			B = B.zfill(Alen)
		else:
			A = A.zfill(Blen)

		print(A)
		print(B)
		#carry to calculate carried number
		carry = 0
		#stores final answer
		ans = ''
		for i in reversed(range(max(Alen,Blen))):
			b1 = A[i]
			b2 = B[i]
			sum = 0
			print(sum)
			#converting string into integer
			a,b = int(b1),int(b2)
			print('a :',a,' || ','b :',b)
			sum = a + b + carry
			print('a+b+carry :',sum)
			carry = sum // 2
			print('carry : ',carry)
			sum = sum % 2
			print('Final Sum :',sum)
			ans += str(sum)
			print('ans :',ans)
		#In order to check MSD digit to check with carry
		if carry == 1:
			ans += str(1)
		return ans[::-1]

s = Solution()
print('Program value : ',s.addBinary('1010110111001101101000','1000011011000000111100110'))
print('Expected Value :',1001110001111010101001110)