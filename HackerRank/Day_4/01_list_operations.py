if __name__ == '__main__':
    list1 = []
    N = int(input())
    for _ in range(N):
        dba = list(input().split())
        list1.append(dba)
    # print(list1)
    res = []
    for i in list1:
        if(i[0]=="insert"):
            res.insert(int(i[1]),int(i[2]))
        elif(i[0]=="print"):
            print(res)
        elif(i[0]=="remove"):
            res.remove(int(i[1]))
        elif(i[0]=="append"):
            res.append(int(i[1]))
        elif(i[0]=="sort"):
            res.sort()
        elif(i[0]=="pop"):
            res.pop()
        elif(i[0]=="reverse"):
            res.reverse()
    