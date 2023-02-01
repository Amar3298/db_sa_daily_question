rec = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    rec.append([name,score])
# rec = [["chi",20.0],["beta",150.0],["alpha",50.0]]
rec.sort(key=lambda x:x[1])
def second_smallest(arr):
    listt = []
    for i in arr:
        listt.append(i[1])
    largest = max(listt)
    sec_lar = max(listt)
    for i in listt:
        if(i<largest and i<sec_lar):
            sec_lar = largest
            largest = i
        elif(i>largest and i<sec_lar):
            sec_lar = i
    return sec_lar
ans_s = second_smallest(rec)
rec.sort()
for i in rec:
    if(i[1]==ans_s):
        print(i[0])