def findDuplicate(arr):
    # Write your code here
    # list1 = [4, 2, 1, 3, 1]
    dict1 = {}
    for i in arr:
        if(i not in dict1.keys()):
            dict1[i] = 1
        else:
            dict1[i] += 1
    for key,value in dict1.items():
        if(value>1):
            return key