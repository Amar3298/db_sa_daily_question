# n = int(input())
# arr = list(map(int,input().split()))
def reverse_arr(n,arr):
    res = arr[::-1]
    for i in res:
        print(i , end=" ")

reverse_arr(8,[7 ,5 ,2 ,11 ,2 ,43 ,1 ,10])