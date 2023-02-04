x,k = map(int,input().split())
polynomial = input()
polynomial =  polynomial.replace("x",f"{x}")
res = eval(polynomial)
if(res==k):
    print(True)
else:
    print(False)