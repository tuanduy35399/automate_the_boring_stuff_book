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


#lay 1 phan area code cua sdt

one_pattern= re.compile(r'(\d{3})-(\d{3}-\d{4})')
match_obj = one_pattern.search('Call me at 415-555-1011')

print(f'415-555-1011 convert to {r"(\d{3})-(\d{3}-\d{4})"} \ngroup(1): {match_obj.group(1)}\ngroup(2): {match_obj.group(2)}\ngroup( ): {match_obj.group()}')

pattern= re.compile(r'do(raemon|or)')
test= pattern.findall('Open the door, doraemon')
print(f'using pipe {test}')

match_interator = pattern.finditer('Open the door, doraemon')
kq = [e.group(0) for e in match_interator]
print(kq)


raw_text="""
Note that, inside the square brackets, the normal regular expression
symbols are not interpreted as such. This means you do not need to escape
characters such as parentheses inside the square brackets if you want to
match literal parentheses. For example, the character class [()] will match
either an open or close parenthesis. You do not need to write this as [\(\)].
By placing a caret character (^) just after the character class’s opening
bracket, you can make a negative character class. A negative character class
will match all the characters that are not in the character class. For exam-
ple, enter the following into the interactive shell:
>>> import re
>>> consonant_pattern = re .compile(r'[^aeiouAEIOU]')
>>> consonant_pattern.findall('RoboCop eats BABY FOOD.')
['R', 'b', 'C', 'p', ' ', 't', 's', ' ', 'B', 'B', 'Y', ' ', 'F', 'D', '.']

"""

clean_text = re.sub(r'[^a-zA-Z0-9\s]', '', raw_text)
pattern= re.compile(r'\w+')
new_text= pattern.findall(raw_text)
print(clean_text)
print(new_text)