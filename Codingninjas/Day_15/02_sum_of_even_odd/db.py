list1 = int(input())
n = len(str(list1))
even = 0 
odd = 0 
for i in range(n):
  a1 = list1%10
  list1 = list1//10
  if(a1%2==0):
    even += a1 
  else:
    odd += a1
print(even,odd)
