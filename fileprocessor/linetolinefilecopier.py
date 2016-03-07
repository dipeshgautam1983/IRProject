#__author__ = 'dipesh'
__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''

import os
def copyfile(sourcefile, destinationfile, linebyline = False):
    sfile = None
    try:
        sfile = open(sourcefile)
    except IOError:
        print('Error: File "' + sourcefile + '" does not exist')
        exit()
    if os.path.exists(destinationfile):
        user_input = input('A file with name "' + destinationfile + '" already exists.\nDo you want to overwrite the existing file (Y/N)?')
        if user_input.lower() != 'y':
            user_input = input("New file path?")
            destinationfile = user_input
    dfile = open(destinationfile,'w')
    if linebyline:

        for line in sfile:
            #print(line + "\n")
            dfile.write(line)
    else:
        print("bytebybyte")

    dfile.flush()
    sfile.close()
    dfile.close()



