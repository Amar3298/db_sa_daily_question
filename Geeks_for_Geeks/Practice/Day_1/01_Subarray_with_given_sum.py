a = [1,2,3,7,5]
a = [135,101,170,125,79,159,163,65,106,146,82,28,162,92,196,143,28,37,192,5,103,154,93,183,22,117,119,96,48,127,172,139,70,113,68,100,36,95,104,12,123,134]
# # a = [1,2,3,4,5,6,7,8,9,10]
sum1 = 468
# sum1 = 15
right = 0
left = 0
current_sum = 0
for i in range(len(a)):
    if(current_sum<sum1):
        current_sum += a[right]
        right += 1
    elif(current_sum>sum1):
        current_sum -= a[left]
        left += 1
    elif(current_sum==sum1):
        break
print(current_sum)
print(a[left:right])
print(left+1,right)
