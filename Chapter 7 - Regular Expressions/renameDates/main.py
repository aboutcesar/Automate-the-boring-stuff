import re
import shutil
import os

datePattern = re.compile(r"""^(.*?)
        ((0|1)?\d)-         #month
        ((0|1|2|3)?\d)-     #Day
        ((19|20)?\d\d)      #year
        (.*?)               #Text after file
""", re.VERBOSE)

#loop over files
for amerFileName in os.listdir('.'):
    print(amerFileName)
    mo = datePattern.search(amerFileName)

    if mo == None:
        continue

    textbefore = mo.group(1)
    monthpart  = mo.group(2)
    daypart    = mo.group(4)
    yearpart   = mo.group(6)
    textafter  = mo.group(8)

    #Euro File name
    euroFilename = textbefore+daypart+'-'+monthpart+'-'+yearpart+textafter

    #Get the full path
    absWorkDir = os.path.abspath('.')
    print(absWorkDir)
    amerFileName = os.path.join(absWorkDir, amerFileName)
    euroFilename = os.path.join(absWorkDir,euroFilename)

    #rename the files
    print(f'Renaming "{amerFileName}" to "{euroFilename}"...')
    shutil.move(amerFileName, euroFilename)

