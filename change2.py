# better use functions. When function exits, all vars or lists will be released.

'''
   @ par: sourcefile
   Create a tempfile if it doesn't exist.

   a .srt file might look like this:

   1
   00:00:00,345 --> 00:00:06,206
   The One Where It All Began

   It deletes the following lines:
   1
   00:00:00,345 --> 00:00:06,206

   A hint for process multiple files in the same folder
   import os.path
   os.listdir (folderPath) returns a list of file names.
'''


import re
import sys
import inspect

p = re.compile('[0-9]+\r\n')
q = re.compile('[0-9]{2}\:')


def cleanfile(sourcefile, tempfile):
    with open(sourcefile) as f:
        with open(tempfile, "w+") as sub:
            for line in f:
                if(line == '\r\n') or (p.match(line)) or (q.match(line)):
                    sub.write('')
                else:
                    sub.write(line)
            sub.close()
            f.close()


if __name__ == "__main__":

    sourcefile = sys.argv[1]
    tempfile = sourcefile + '-output'
    cleanfile(sourcefile, tempfile)
