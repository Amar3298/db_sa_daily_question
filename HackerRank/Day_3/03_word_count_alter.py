if __name__=="__main__":
    # list1 = ["bcdef","abcdefg","bcde","bcdef"]
    list1 = []
    for i in range(int(input())):
        dba = input()
        list1.append(dba)
    set_l = list1
    rep_l = []
    for i in list1:
        if(i not in rep_l):
            rep_l.append(i)
    print(len(rep_l))
    for i in rep_l:
        print(list1.count(i),end=" ")