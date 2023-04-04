s = "ssssss"
"""
1. First we are taking list we will iterate through the string
2. We will see if the i is present in the list if yes clear the list and append the i in the list if not just append the i in the list 
3. At the end we check if the list is not empty that means there is one more substring in the list that word count is added to the count 
Refer:- https://www.youtube.com/watch?v=SXFWR6EIQw4
"""
res_set = []
res = 0
for i in s:
    if(i in res_set):
        res_set.clear()
        res_set.append(i)
        res += 1
    else:
        res_set.append(i)
if(len(res_set)>0):
    res+= 1
print(res)