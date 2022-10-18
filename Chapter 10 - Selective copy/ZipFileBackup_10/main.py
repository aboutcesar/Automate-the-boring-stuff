#! Creates zip file backups
import os, zipfile

def backupToZip(folder):  #takes string file to the folder that needs back up
    #back up entire contents to the zipFile

    folder = os.path.abspath(folder)
    
    #what files should this be used on

    #Folders that exists already (since we can make different folders for everytime we want to back things up)
    Number = 1
    while True:

        zipFileName = os.path.basename(folder) + '_' + str(Number) + '.zip'
        if not os.path.exists(zipFileName):
            break

        Number += 1

    #Create the zipfile

    print(f'Creating ZipFile {zipFileName}... ')
    backupZip = zipfile.ZipFile(zipFileName, 'w')

    #walk the folder
    for folderName, subfolders, filenames in os.walk(folder):
        print(f'Adding files in: {folderName}')
        #add the current folder
        backupZip.write(folderName)

        #Add all the files in this folder to the zipFile
        for filename in filenames:
            newBase = os.path.basename(filename)
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue

            backupZip.write(os.path.join(folderName, filename))
    backupZip.close()
    print('done')


backupToZip('C:\\Users\\jguti\\Desktop\\Posters')


