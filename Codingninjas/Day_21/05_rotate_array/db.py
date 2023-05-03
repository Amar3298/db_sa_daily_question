# n = int(input())
# arr = list(map(int,input().split()))
# rotate = int(input())
def rotate_arr(n,arr,rotate):
    right = arr[:rotate]
    left = arr[rotate:]
    res = left + right
    for i in res:
        print(i , end=" ")
rotate_arr(8,[7 ,5 ,2 ,11 ,2 ,43 ,1 ,1],2)
