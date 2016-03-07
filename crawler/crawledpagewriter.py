#__author__ = 'dipesh'
__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''

import os
def writetofile(text, destinationfolder, filename, sourceurl=""):
    #print("write to file ", text)
    filename = destinationfolder.strip("/") + "/" + filename

    destfile = None
    try:
        if os.path.exists(filename):
            raise Exception('crawledpagewriter.py; writetofile: A file with name: "' + filename + '" already exists')
    except Exception as e:
        raise e
    try:
        destfile = open(filename,'w')
        if sourceurl !="":
            destfile.write("#" + sourceurl + "\n")
        destfile.write(text)
        destfile.flush()

    except Exception as e:
        if destfile != None and not destfile.closed:
            #print("ERROR")
            destfile.close()
            #print(destfile)
            os.remove(filename)
        raise e

    finally:
        #print("finally")
        if destfile != None and not destfile.closed:
            destfile.close()

