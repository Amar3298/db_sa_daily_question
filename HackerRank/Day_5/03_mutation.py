def mutate_string(string, position, character):
    res = ""
    left_a = string[:position]
    res += left_a
    res += character
    res += string[position+1:]
    return res

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)