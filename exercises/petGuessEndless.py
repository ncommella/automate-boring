pets = ['luger', 'roman', 'roxy']

while True:
    print('Please enter a pet name (or enter q to quit):')
    inquiry = input()

    if inquiry.lower() == 'q':
        break
    
    elif inquiry.lower() not in pets:
        print('I do NOT have a pet named ' + inquiry)
    
    else:
        print('I do have a pet named ' + inquiry)
