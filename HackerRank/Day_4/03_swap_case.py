# a = "abAB"
# str1 = ""
# for i in a:
#     if(i.isupper()):
#         str1+=i.lower()
#     else:
#         str1+= i.upper()
# print(str1)
def swap_case(s):
    str1 = ""
    for i in s:
        if(i.isupper()):
            str1+= i.lower()
        else:
            str1 += i.upper()
    return str1

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)