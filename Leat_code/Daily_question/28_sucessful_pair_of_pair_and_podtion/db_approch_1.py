spells = [3,1,2]
potions = [8,5,8]
success = 16
res = []
for i in spells:
    tem_res = []
    count = 0
    for j in potions:
        if(i*j>=success):
            count += 1
    res.append(count)
print(res)