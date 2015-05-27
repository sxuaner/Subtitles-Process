import os

def merge(sourcefile, merged):
    with open(sourcefile) as f:
        for line in f:
            merged.write(line)
        f.close()


if __name__  == "__main__":
    dirPath = os.getcwd()
    merged = open(dirPath + '/merged', 'a')

    fileIndex = []
    for i in os.listdir(dirPath):
        if(os.path.isfile(i) and i != "merge.py"):
            fileIndex.append(i)

    for n in fileIndex:
        merge(n,merged)
        print n
    merged.close()
