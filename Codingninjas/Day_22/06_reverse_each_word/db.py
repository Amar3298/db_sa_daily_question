def reverseEachWord(string) :
    string = map(lambda x: x[::-1], string.split(' '))

    return ' '.join(string)
print(reverseEachWord("Welcome to Coding Ninjas"))