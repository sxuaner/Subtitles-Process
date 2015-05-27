# better use functions. When function exits, all vars or lists will be released.
'''
$python change2.py :
Read all file in current folder where change2.py locates in.

$python change2.py sourcefile:
Read 'file1' in and output to file named "file1-output"


'''

'''
   A .srt file might look like this:

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
import os


p = re.compile('[0-9]+\r\n')
q = re.compile('[0-9]{2}\:')

'''

@par  sourcefile
@par  tempfile = sourcefile + 'output'  Create a tempfile if it doesn't exist.
@flow read a line in sourcefile, if it matches '\r\n' or p or q, write a blank line into output.
      Otherwise copy the line into output.

'''
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

    argumentSpec = len(sys.argv)

    if(argumentSpec == 2):
        sourcefile = sys.argv[1]
        cleanfile(sourcefile, sourcefile + 'output')

    elif(argumentSpec == 1):
        dirPath = os.getcwd()
        tmpPath = dirPath + '/temp'
        if not os.path.exists(tmpPath):
            os.makedirs(tmpPath)

        fileIndex = []
        for i in os.listdir(dirPath):
            if(os.path.isfile(i) and i != 'change2.py'):
                fileIndex.append(i)

        counter = 0;
        for f in fileIndex:
            output = tmpPath + '/' + f + '-output'
            print output
            cleanfile(f, output)
            counter = counter + 1
        print "In total:", counter
