#__author__ = 'dipesh'
__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''
__preprocessed_dir__ = "preprocessed_docs"
__outputdir__ = "documents"

#__preprocessed_dir__ = "C:/Users/dipesh/Desktop/all/crawldocs/preproc"
#__outputdir__ = "C:/Users/dipesh/Desktop/all/crawldocs/raw"

__logdir__ = "log"
__stopwordfile__ = "resources/english.stopwords.txt"
__searchpagetemplate__ = "searchengine/pagetemplate.html"
__crawlingdomain__ = {".com",".edu",".gov",".net",".org", ".int", }
__badfiletype__ = [".jpg", ".mpeg", ".wmv", ".png", ".exe", ".js", ".bmp", ".mp3", ".mpeg", ".tif", ".gif", ".jar", ".zip", ".rpm", ".tar",".xml"]
__badurltype__ = ["tel:","mailto:","ftp:"]
__rooturls__ = ["memphis.edu"]
#__rooturls__ = ["ioe.edu"]
__restrictdomain__ = True
__saverawpage__ = False ##set False to remove html tags in downloaded files
__crawldelay__ = 5
__maxthread__ = 500
__maxjobsize__ = 100
__crawldepth__ = 1000
__minwordinpage__ = 50
__verbose__ = True
__pushtoposting__ = False # set this to true if you want to create index on fly, without saving files.
# However you have to calculate document length which is not possible untill crawlling is completed.
import re
def getstoplist():
    stplist = open(__stopwordfile__)
    stoplist ={}
    for word in stplist:
        stoplist[re.sub(r"[\r\n]+","",word.lower())]=1
    stplist.close()
    return stoplist

__stoplist__ = getstoplist()

