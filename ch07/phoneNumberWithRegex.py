#!/usr/bin/python3
import re
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
phoneNumberRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
print('Phone numbers found: ' + str(phoneNumberRegex.findall(message)))
