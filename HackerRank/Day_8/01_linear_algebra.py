import numpy
list1 = []
for _ in range(int(input())):
    tempa = list(map(float,input().split()))
    list1.append(tempa)
res = numpy.linalg.det(list1)
res_str = str(res)
str1 = res_str.split(".")
if(len(str1[1])==1):
    print(res)
else:
    print("%.2f"%res)
