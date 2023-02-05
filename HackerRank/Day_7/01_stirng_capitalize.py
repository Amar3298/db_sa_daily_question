def solve(s):
    res_list = s.split(" ")
    rJ = []
    for i in res_list:
        rJ.append(i.capitalize())
    join_a = " "
    res = join_a.join(rJ)
    return res
if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)