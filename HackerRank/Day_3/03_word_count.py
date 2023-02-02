if __name__=="__main__":
    from collections import Counter
    list1 = []
    for i in range(int(input())):
        dba = input()
        list1.append(dba)
    ans = Counter(list1)
    print(len(ans.values()))
    print(*(ans.values())) # this is called unpack operator
