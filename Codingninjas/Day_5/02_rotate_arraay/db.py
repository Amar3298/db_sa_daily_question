n = int(input())
list1 = list(map(int,input().split()))
key = int(input())

rotate = list1[:key]
right_part = list1[key:]
res = right_part + rotate
for i in res:
  print(i,end=" ")