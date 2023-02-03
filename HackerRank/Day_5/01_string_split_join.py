def split_and_join(line):
    # write your code here
    list1 = line.split(" ")
    join_db = "-"
    res = join_db.join(list1)
    return res
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)