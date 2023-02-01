if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    list_A = student_marks[query_name]
    res = sum(list_A)/len(list_A)
    print("%.2f"%res)