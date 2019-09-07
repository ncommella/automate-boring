import random

def getAnswer(ansNum):
    if ansNum == 1:
        return 'It is certain.'
    elif ansNum == 2:
        return 'It is decidedly so'
    elif ansNum == 3:
        return 'Yes'
    elif ansNum == 4:
        return 'Reply hazy, try again'
    elif ansNum == 5:
        return 'Try again later'
    elif ansNum == 6:
        return 'Concentrate and ask again'
    elif ansNum == 7:
        return 'My reply is no'
    elif ansNum == 8:
        return 'Outlook not so good'
    elif ansNum == 9:
        return 'Very doubtful'

#generates random number between 1-9, passes it to getAnswer(), and prints returned statement
print(getAnswer(random.randint(1,9)))
    
