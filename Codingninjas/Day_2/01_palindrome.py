def checkPalindrome(s):
    li = []
    s = s.lower()
    for i in s:
        if i.isalnum():
            li.append(i)
    if li == li[::-1]:
        return True
    else:
        return False