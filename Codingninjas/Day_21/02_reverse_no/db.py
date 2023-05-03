def reverseNumber(n):

	# Write your code here.
	res = 0
	while(n!=0):
		ta = n % 10
		n = n // 10
		res = res * 10 + ta

	return res

print(reverseNumber(104000))