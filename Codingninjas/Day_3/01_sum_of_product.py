def sumOrProduct(n, q):
    prod = 1
    if(q==1):
        res = n*(n+1)//2
        return res
    else:
        for i in range(1,n+1):
            prod = (prod*i)%1000000007   
        return prod