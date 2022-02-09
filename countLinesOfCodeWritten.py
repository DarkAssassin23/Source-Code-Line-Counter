import sys, os, subprocess

dirList = ""
typesOfFiles = []

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


files = []
try:
    
    loadFilesTypes()
    # Get all of the files in the directory
    while len(dirList) > 0:
        for (dirpath, dirnames, filenames) in os.walk(dirList.pop()):
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

