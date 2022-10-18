#! Selective Copy
import shutil, os

def selectiveCopy(folder, destination):
    for foldername, subfolders, fileNames in os.walk(folder):
        print(f'this folder is {foldername}')
        for fileName in fileNames:
            print(f'This file is: {fileName}')
            if fileName.endswith('jpg'):
                print('copying %s from %s to %s...' % (fileName, folder, destination))
                shutil.copy(os.path.join(foldername,fileName), destination)




selectiveCopy('C:\\Users\\jguti\\Desktop\\Posters','C:\\Users\\jguti\\Desktop\\Posters\\Shutil')

