def reverseStringWordWise(string):
    #Your code goes here
    list1 = string.split(" ")
    rev_list = list1[::-1]
    res = " ".join(rev_list)
    return res

res = reverseStringWordWise("Welcome to Coding Ninjas")
print(res)