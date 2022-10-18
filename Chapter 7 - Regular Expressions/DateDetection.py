import re, pyperclip

#check for valid date

date = re.compile(r'''(
    (0[9]|1[012])  # month catches 0-9 and 10-12
    (/-.)          #seperator 
    (0?[1-9]|[12][0-9]|3[01])        #day 
    (/-.)          #
    ([12]\d{3})        #

)''', re.VERBOSE)

text = str(pyperclip.paste())
#print the date, each group

matches = []

for groups in date.findall(text):
    matches.append(groups)

print(matches)