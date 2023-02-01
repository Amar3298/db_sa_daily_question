s = "N2 i&nJA?a& jnI2n"
s = s.lower()
list1 = []
list1[:] = s
join_a = ""
for i in list1:
    if(i!=" "):
        join_a+=i
rev = join_a[::-1]
print(rev,join_a)