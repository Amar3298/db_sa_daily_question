def countBits(n):
    ab = bin(n).replace("0b", "")
    count = 0
    for i in ab:
        if(i=='1'):
            count += 1
    return count

print(countBits(5))