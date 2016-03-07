#__author__ = 'dipesh'
__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''
from lib import webpagereader
from crawllogger import logger
def readtextfromurl(sourceurl):

    try:
        if ".pdf" in sourceurl.split('/')[-1]:
            return webpagereader.readpdftext(sourceurl)
        elif".ppt" in sourceurl.split('/')[-1]:
            raise Exception("Not supported in version", "Page can not be read in this version of crawler")
        else:
            return webpagereader.readhtmlpage(sourceurl) #default value of removetags=False
    except Exception as e:
        #print("Exception in urlcontentreader:", e)
        logger.writelog("Exception in urlcontentreader: "+ sourceurl + " " + str( e))
        return ""