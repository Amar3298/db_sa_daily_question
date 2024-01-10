N = 6
K = 3
# arr = [2, 7, 6, 1, 4, 5]
arr = [5,2,1,4,7,8,2,5]

def func_mod(n):
  """
  Function 
  input: N(Number) 
  output: reminder (that is divided by k)
  """
  return (n%K)

"""
# testing the func_mod function 

for i in arr:
  print(func_mod(i),end=" ")

end of testig of func_mod function
"""

prefix_sum = []
for i in range(N+2):
  prefix_sum.append(sum(arr[:i+1]))
  """
  Testing the prefix sum 
  # print(arr[:i+1])
  # print(sum(arr[:i+1]),end=",",)
  
  End of testing the prefix sum 
  """
reminder_arr = list(map(func_mod,prefix_sum))
print(reminder_arr)
# unique_elements = []
# for i in reminder_arr:
#   if i not in unique_elements:
#     unique_elements.append(i)

logest_arr = 0
i = 0
j = N+1 
while(j>=i):
  print(reminder_arr[i],reminder_arr[j])
  if(reminder_arr[i]==reminder_arr[j]):
    i+=1 
    j-=1
    tmp = j-i
    if(tmp>logest_arr):
      logest_arr = tmp 
  i+=1 
  j-=1
print(logest_arr)