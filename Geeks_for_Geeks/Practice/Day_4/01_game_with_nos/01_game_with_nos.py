def game_with_number (arr,  n) : 
    res = []
    for i in range(n-1):
        res.append(arr[i]^arr[i+1])
    res.append(arr[-1])
    return res

for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    res = game_with_number(arr, n);
    print(*res)
