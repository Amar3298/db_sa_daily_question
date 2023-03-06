def decode(x):
    if x==".-":
        return 'a'
    elif x=="-...":
        return 'b'
    elif x=="-.-.":
        return 'c'
    elif x=="-..":
        return 'd'
    elif x==".":
        return 'e'
    elif x=="..-.":
        return 'f'
    elif x=="--.":
        return 'g'
    elif x=="....":
        return 'h'
    elif x=="..":
        return 'i'
    elif x==".---":
        return 'j'
    elif x=="-.-":
        return 'k'
    elif x==".-..":
        return 'l'
    elif x=="--":
        return 'm'
    elif x=="-.":
        return 'n'
    elif x=="---":
        return 'o'
    elif x==".--.":
        return 'p'
    elif x=="--.-":
        return 'q'
    elif x==".-.":
        return 'r'
    elif x=="...":
        return 's'
    elif x=="-":
        return 't'
    elif x=="..-":
        return 'u'
    elif x=="...-":
        return 'v'
    elif x==".--":
        return 'w'
    elif x=="-..-":
        return 'x'
    elif x=="-.--":
        return 'y'
    elif x=="--..":
        return 'z'
    elif x==".----":
        return '1'
    elif x=="..---":
        return '2'
    elif x=="...--":
        return '3'
    elif x=="....-":
        return '4'
    elif x==".....":
        return '5'
    elif x=="-....":
        return '6'
    elif x=="--...":
        return '7'
    elif x=="---..":
        return '8'
    elif x=="----.":
        return '9'
    elif x=='-----':
        return '0'
def morseToEnglish(morsecode):
    list1 = morsecode.split(" ")
    list3 = map(lambda x:decode(x),list1)

    bl = ""
    res = bl.join(list3)
    return res

res = morseToEnglish("-.-. --- -.. .. -. --.")
print(res)
