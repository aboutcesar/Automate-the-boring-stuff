from pathlib import Path
import os, re

#txtFiles = list(p.glob('*.txt'))
#print(txtFiles)

p = Path('C:\\Users\\jguti\\PycharmProjects\\RegexSearch')
userRegex = re.compile(input('Enter a Regular Expression: \n'))

found = []
nomatch = []

for file in p.glob('*.txt'):
    print(file)
    hFile = file.open()
    txtfile = hFile.read()
    print(txtfile)

    tally = []
    for match in re.findall(matchReg , txtfile):
        tally.append(match)

    filename = file.name
    if tally:
        a = f'Matches in \"{filename}\" are {tally}'
        found.append(a)
    else:
        # b = f'There were no matches found in \"{filename}\"'
        nomatch.append(filename)

print('\n'.join(found))
print('\nThere were no matches found for: ', *nomatch, sep='\n')