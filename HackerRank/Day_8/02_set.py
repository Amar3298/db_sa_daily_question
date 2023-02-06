def average(array):
    # your code goes 
    set_arr = set(array)
    res = sum(set_arr)/len(set_arr)
    return res

if __name__ == '__main__':
    # n = int(input())
    # arr = list(map(int, input().split()))
    arr = [161,182,161,154,176,170,167,171,170,174]
    result = average(arr)
    print(result)