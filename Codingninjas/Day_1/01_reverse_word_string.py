def reverseString(str):
	#Write your code here.
	rev1 = str.split(" ")
	res = rev1[::-1]
	join_a = " "
	sa_db = join_a.join(res)
	return sa_db