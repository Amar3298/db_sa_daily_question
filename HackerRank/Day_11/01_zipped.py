m,n = map(int,input().split())
line = []
for _ in range(n):
    line.append(list(map(float,input().strip().split())))

ls = list(zip(*line))

for i in range(m):
    print(round(sum(ls[i])/n,1))
