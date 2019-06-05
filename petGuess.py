pets = ['Luger', 'Roman', 'Roxy']

print('Please enter a pet name:')
inquiry = input()
if inquiry not in pets:
    print('I do NOT have a pet named ' + inquiry)
else:
    print('I do have a pet named ' + inquiry)
