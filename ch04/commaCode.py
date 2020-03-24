#!/usr/bin/python3
def listToString (list):
    newString = ''
    for w in list:
        if w != list[-1]:
            newString += w + ', '
        else:
            newString += 'and ' + list[-1]
            break

    return newString

spam = ['apples', 'bananas', 'tofu', 'cats']
print(listToString(spam))
