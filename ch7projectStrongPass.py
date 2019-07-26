import re

word = input('what is your password')
count = 0
countl = 0
num = 0
for i in word:
    print(i)
    if i.isupper():
        count += 1
    elif i.islower():
        countl += 1
    elif i.isdigit():
        num +=1
print(count, countl, num)
if (count > 0) & (countl>6) & (num >0):
    passwordregex = re.compile(r'(.*)')
    mo = passwordregex.search(word)
    print(mo.group())
    print('Password is valid')
else:
    print('not a good password')
passwordrege = re.compile(r'''(
        ^(?=.*[A-Z])             # at least two capital letters
        (?=.*[!@#$&*])                     # at least one of these special characters
        (?=.*[0-9])                 # at least two numeric digits
         (?=.*[a-z].*[a-z].*[a-z].*[a-z].*[a-z].*[a-z].*[a-z])          # at least 7 lower case letters
         .{10,}                              # at least 10 total digits
    $
    )''', re.VERBOSE)
mor = passwordrege.search(word)
print(mo.group())
print('valid')