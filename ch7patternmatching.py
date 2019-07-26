#regex is a regular expression  \d = digital character
# | means first word will be group only so r'batman|tina fey' group() = batman but switch words tina fey prints
# ? = match zero or one to what this is in front of. = non greedy mode
# * means whats is in parethesis before the * can be repeated and if seen in the text can be repeated at long as its in the text in parethesis is optional
# + is not optional bu tacts like a *
# USING A ^ MEANS EVERYTHING THAT IS NOT IN YOUR REGEX COMPILE STATEMENT IS PRINTED OR PUT INTO A LIST VIA FINALL

import re

phoneNumRegex = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
letter = re.compile(r'(ha){2,6}?')
word = re.compile(r'\D\D\D\D\D\D')
more = word.search("boi you a beotch")
print("lil wayne "+ more.group())
mo = phoneNumRegex.search('My number is (415)-678-3423.')
mor = letter.search('hahaha you are so funny haha, and yeah ha')

print('phone number found: '+ mo.group(1) + mor.group())
print(mor.group)
print(mo.group(2))
print(mo.group())

#message = 'call me at work 360-503-3937, or my work cell is 3557-767-8697'
#for i in range(len((message)):
   # chunk = message[i:i+12]
  #  if isPhoneNumber(chunk):
      #  print('number found'+ chunk)
print('done')

numregex = re.compile(r'First Name: (.*) Last Name: (.*)')
moree = numregex.search('First Name: Hunter Last Name: Wickman')
print('yut ' + moree.group())
