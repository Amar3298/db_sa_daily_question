def findThirdLagrest(arr):
	# Write your code here
	arr.sort()
	r = tuple(arr)
	res = r[-3]
	return res

print(findThirdLagrest([2,6,7,4,9]))