if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    largest = min(arr)
    second_largest = min(arr)
    for i in arr:
        if(i>largest and i>second_largest):
            second_largest = largest
            largest = i
        elif(i<largest and i>second_largest):
            second_largest = i
    print(second_largest)
    # arr = [2,3,10,15,13,5,6,6]