def countWords(string) :
	# Your code goes here
	list1 = string.split(" ")
	return len(list1)
res = countWords("Coding Ninjas!")
print(res)