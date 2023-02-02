from collections import Counter
list1 = ["a","b","c","a"]
# here we have list of alphabetes some are repeating some are not 
# we want the no of each letter
ans = Counter(list1) # it will give dictionary of key value pair
print(ans)

# now we just want values we will use ans.values()
dic_val = ans.values()
print(dic_val)

# now we will use unpack operator to print the values
print(*dic_val)
