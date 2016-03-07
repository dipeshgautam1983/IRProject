#__author__ = 'dipesh'

__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''

import time

from lib import htmlparser,urlcontentreader
from crawler import globals, crawledpagewriter
from crawllogger import logger


def crawlthrough(urlslevels, crawldepth, threadid=0, savedir=None):

    load = len(urlslevels)
    #print("Load ", load, urlslevels,"\n\n", globals.geturlqueue())
    for i in range(0,load):
        url,level= urlslevels[i]

        '''crawl through the url'''
        try:
            logger.writelog("Thread " + str(threadid) + ", Total load=" + str(load) + " Crawled=" + str(i) + ", Crawling " + url)

            #print("crawling ", url)
            rawtext = urlcontentreader.readtextfromurl(url)
            #print("attempted crawling ", url)
            #print(url, "\n", rawtext,"\n")

            #newurls, text = htmlparser.fetch.fetchurlandtext(url,True)
            newurls, cleantext = htmlparser.getcleantextandurls(rawtext,url)
            #print("new len:", len(newurls),newurls)

            text = rawtext
            if not globals.issaverawtext():#if set to clean html tags
                text = cleantext

            '''
            print(threadid, "here")
            print(text)
            print(threadid,"there")
            '''
            level += 1
            if len(newurls) > 0 and level<=crawldepth:

                globals.enqueueurls(newurls,level)
            if cleantext.count(" ")>=globals.getminpagesize(): ##save the page content if it contains atleast minimum number of words
                #print("here is it")
                if savedir != None and savedir != "":
                    crawledpagewriter.writetofile(text, savedir,str(globals.generateuniquenumber())+".txt", url)
                if globals.pushtoposting():
                    globals.updateposting(text,url)
                else:
                    globals.updatesuccesscount()
            else:
                logger.writelog("Thread " + str(threadid)+ " Error in urlcrawler: too few words in page or page cannot be read")
        except Exception as e:
            logger.writelog("Thread " + str(threadid) + " " + str(e) + " Exception; Exception occured in urlcrawler.")
            pass
        time.sleep(globals.getcrawldelay())
    globals.deletefrombusythreadlist(threadid)