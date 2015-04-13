# better use functions. When function exits, all vars or lists will be released.

import re
'''
import os.path
os.listdir (folderPath) returns a list of file names.
'''
sourcefile="./friends01.srt"
tempfile="./temp01.srt"

p=re.compile('[0-9]+\r\n')
q=re.compile('[0-9]{2}\:')

def cleanfile( sourcefile, tempfile):
    with open(sourcefile) as f:
        with open(tempfile,"r+") as sub:
            for line in f:
                if(line=='\r\n') or (p.match(line)) or (q.match(line)):
                    sub.write('')
                else:
                    sub.write(line)
        sub.close()
    f.close()


if __name__=="__main__":
    cleanfile(sourcefile,tempfile)
