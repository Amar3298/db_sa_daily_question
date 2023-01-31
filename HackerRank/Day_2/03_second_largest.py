arr = [2,3,10,15,13,5,6,6]
larg = min(arr)
second_l = min(arr)
for i in arr:
    if(i>larg and i>second_l):
        second_l = larg
        larg = i
    elif(i<larg and i>second_l):
        second_l = i
print(second_l)