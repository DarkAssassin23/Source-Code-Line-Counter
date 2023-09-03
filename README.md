# Source Code Line Counter

About
-----------
- This is a customizable script which recursively counts every line of code you've written in a given directory
- It reads in a confguration file (fileTypes.txt) which contains all the file types for the source code files you'd like it to count
- You can also add any files or directories you would like to exclude in an 'exclude.txt' file

__________________________


Usage
----------
By default, the script executes in its current directory. However, you can pass in the directory you would like it to scan as a parameter
```bash
python3 countLinesOfCodeWritten.py
```
```bash
python3 countLinesOfCodeWritten.py /super/cool/project/source_code
```

Excluding Files and Directories
---------------
If you would like to exclude individual files, simply add the name of the file to the exclude.txt file with its extention

Ex. ```someFile.h```

If you would like to exclude an entire directory, add the full path to the directory from the root of your project

Ex. Your root directory is the following ```/super/cool/project/source_code```. You have a subdirectory you want to exclude located at
```/super/cool/project/source_code/headers/includes```. To exclude it, add the following to your exclude.txt file: ```headers/includes```
