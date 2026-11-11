def is_phone_number(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3]!='-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
                    return False
    if text[7]!='-':
            return False
    for i in range(8, 12): # The next four characters must be numbers.
        if not text[i].isdecimal():
            return False
    return True

# print('Is 415-555-4242 a phone number?', is_phone_number('415-555-4242'))
# print(is_phone_number('415-555-4242'))
# print('Is Moshi moshi a phone number?', is_phone_number('Moshi moshi'))
# print(is_phone_number('Moshi moshi'))

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    segment = message[i:i+12]
    if is_phone_number(segment):
        print('Phone number found: ' + segment)
print('Done')

import re 

phone_pattern= re.compile(r'\d{3}-\d{3}-\d{4}')
match_obj= phone_pattern.search('Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.')

print(f'Dung search + match_obj.group() :{match_obj.group()}')

print(f'Dung findall(): {phone_pattern.findall('Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.')}.')
