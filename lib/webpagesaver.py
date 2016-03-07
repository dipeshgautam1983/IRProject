#__author__ = 'dipesh'
__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''

import urllib.request

import lib.htmltagremover


def savewebpage(sourceurl, destinationfile, removetag = False):
    response = urllib.request.urlopen(sourceurl)
    dfile = open(destinationfile,'w')
    content = ""
    if not removetag:
        pagecontent = response.readlines()
        for line in pagecontent:
            content += line.decode("utf-8")
    else:
        pagecontent = lib.htmltagremover.removetags(response.read())
        content = pagecontent


    dfile.write(content)
    dfile.flush()
    response.close()
    dfile.close()
