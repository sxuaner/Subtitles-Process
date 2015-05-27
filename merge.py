'''
This program merges all files in current folder excluding merge.py itself.
'''
import os

def merge(sourcefile, merged):
    with open(sourcefile) as f:
        for line in f:
            merged.write(line)
        f.close()


if __name__  == "__main__":
    dirPath = os.getcwd()

    fileIndex = []
    for i in os.listdir(dirPath):
        if(os.path.isfile(i) and i != "merge.py"):
            fileIndex.append(i)

    merged = open(dirPath + '/merged', 'a')
    for n in fileIndex:
        merge(n,merged)
        print n
    merged.close()
