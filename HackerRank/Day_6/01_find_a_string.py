# str1 = "ABCDCDC"
# sub_str = "CDC"
# count = 0
# for i in range(len(str1)):
#     if(sub_str==str1[i:i+3]):
#         count+=1
# print(count)

def count_substring(string, sub_string):
    count1 = 0
    for i in range(len(string)):
        if(sub_string==string[i:i+len(sub_string)]):
            count1 += 1
    return count1

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)