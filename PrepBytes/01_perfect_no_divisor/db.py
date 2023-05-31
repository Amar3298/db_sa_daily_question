def perfect_no(n):
  res = 0
  for i in range(1,n):
    if(n%i==0):
      res += i
  if(res==n):
    return "true"
  else:
    return "false"
n = int(input())
for i in range(n):
  t = int(input())
  print(perfect_no(t))

"""
Input
        2
        28
        96
Output
        true
        false
"""