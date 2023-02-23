def completeSum(a: List[int], n: int)-> List[int]:
    res = []
    for i in range(n):
        temp = sum(a[:i+1])
        res.append(int(temp))
    return res