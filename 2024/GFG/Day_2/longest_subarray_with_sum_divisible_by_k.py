N = 7
K = 3
arr = [-2, 2, -5, 12, -11, -1, 7]
# arr = [5,2,1,4,7,8,2,5]

def func_mod(n):
  """
  Function 
  input: N(Number) 
  output: reminder (that is divided by k)
  """
  return (n%K)
def fin_longest_dis(lst,n):
  """
  input: arr and number for which we want to find the first index and last index
  output: longest sub array that is divisible by k
  """
#   looping in forward direction
  len_arr = len(lst)-1
  first_index = 0
  last_index = len_arr
  for i in range(len_arr):
    if(lst[i]==n):
      first_index = i 
      break

# looping in reverse direction
  j = len_arr
  while(j>=0):
    if(lst[j]==n):
      last_index = j 
      break
    j-=1
  return last_index-first_index
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
# print(reminder_arr)
unique_elements = []
for i in reminder_arr:
  if i not in unique_elements:
    unique_elements.append(i)
    

res = []
for i in unique_elements:
  res.append(fin_longest_dis(reminder_arr,i))
print(res)

