#__author__ = 'dipesh'
__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''

import urllib.request
import lib.htmltagremover
from crawllogger import logger
def readhtmlpage(sourceurl, removetag = False):
    '''
    headers = {
        'User-Agent': 'Student Crawler from University of Memphis',
        'From': 'dgautam@memphis.edu'
    }
    '''

    #response = urllib.request.get(sourceurl, headers=headers)
    #req = urllib.request.Request(sourceurl,headers)
    #response = urllib.request.urlopen(req)
    response = urllib.request.urlopen(sourceurl)
    content = ""
    if not removetag:
        content = response.read().decode("utf-8",errors='ignore')
        #content = content.encode("ascii","ignore")
    else:
        content = lib.htmltagremover.removetags(response.read().decode("utf-8"))
        #content = content.encode("ascii","ignore")
    response.close()
    #print("URLLLLLLLLLLL ",response.url)
    return content


from fileprocessor import pdftextreader
import io, urllib.request
import os

def readpdftext(sourceurl):
    tempfile = None
    tempfilename = "temp/" + sourceurl.split('/')[-1]
    try:
        response = urllib.request.urlopen(sourceurl)

        #print(tempfilename)
        temppdffile = open(tempfilename, 'wb')
        temppdffile.write(response.read())
        temppdffile.flush()
        temppdffile.close()
        content = pdftextreader.readpdftext(tempfilename)
    except Exception as e:
        logger.writelog(str(e) + " Exception; Exception occured in webpagereader.readpdftext.")
        pass

    finally:
        if tempfile != None and not tempfile.closed:
            tempfile.close()
        os.remove(tempfilename)
    return content

def readpptpage(sourceurl):
    return ""

'''below are the test codes'''

#print(readhtmlpage("http://www.cs.memphis.edu/~vrus/teaching/ir-websearch",True))