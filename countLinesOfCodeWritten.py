#!/usr/bin/env python3
import sys, os, subprocess

dirList = ""
typesOfFiles = []
excluded = []

if(len(sys.argv) == 2):
    dirList = [sys.argv[1]]
else:
    dirList = [os.path.expanduser("./")]

linesOfCode = 0
def loadFilesTypes():
    try:
        contents = []
        with open("./fileTypes.txt","r") as f:
            contents = f.readlines()
        for x in contents:
            typesOfFiles.append(x.strip())
        return True
    except:
        print("ERROR: unable to read fileTypes.txt, make sure it exists in the same directory as this file")
        return False

# If you are excluding directories, you need the full path to the directory
# from your root directory. If you want to exclude individual files, just put the filename
# plus its extention, no need for the full path.
# Ex. your root directory is src and you have a subfolder inside your
# headers folder called includes that you wanted to exclude, you would need to 
# add 'headers/includes' (minus the quotes) to your exclude.txt file to exclude that
# entire directory
def loadExcludeFiles():
    if(os.path.exists("./exclude.txt")):
        try:
            contents = []
            with open("./exclude.txt","r") as f:
                contents = f.readlines()
            for x in contents:
                excluded.append(x.strip())
            return True
        except:
            print("ERROR: unable to read exclude.txt, make sure it exists in the same directory as this file")
            return False

files = []
try:
    
    loadFilesTypes()
    loadExcludeFiles()
    isFirstLoop = True
    basePath = ""
    # Get all of the files in the directory
    while len(dirList) > 0:
        for (dirpath, dirnames, filenames) in os.walk(dirList.pop()):
            if(isFirstLoop):
                basePath = dirpath+"/"
                isFirstLoop = False
            excludeDir = False
            for x in excluded:
                if(dirpath == basePath+x):
                    excludeDir = True
                    break
                try:
                    filenames.remove(x)
                except:
                    pass
            if(not excludeDir):
                dirList.extend(dirnames)
                files.extend(map(lambda n: os.path.join(*n), zip([dirpath] * len(filenames), filenames)))

    for x in files:
        for i in typesOfFiles:
            if(x.endswith(i)):
                cmd = "cat "+ x +" | wc -l" # command to get the lines of code for each file
                proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE) # pipes output to proc
                linesOfCode += (int)(proc.stdout.read()) # casts the output as an int then adds it to the total
                break

    print("Total Lines of code: "+str(linesOfCode))

    if(linesOfCode == 0):
        print("Make sure the directory you entered is correct")
        print("Also make sure there are code files in the directory you entered")

except Exception as e:
    print(e)
    print("Unable to compute the total number lines of code")
    print("If you manually entered a path name, make sure it is correct")
