#__author__ = 'dipesh'
__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''
from collections import deque
import threading

from indexer import invertedindex
from resources import settings
from crawllogger import logger

'''define global variables '''
__urlqueue__ = deque()
__queuedurl__ = {}#__queuedurl__ provides global lookup for unique urls that are already queued or crawled
__failedurl__ = {}
__posting__={}
__doclensqr__ = {}
__docurlmap__ = {}
__successcount__ = 0

__totalthreaddispatch__ = 0

___busythreadlist__ = {}


def getbusythreadlist():
    global ___busythreadlist__
    return ___busythreadlist__

def getposting():
    global __posting__
    return __posting__

def getdoclensqrlist():
    global __doclensqr__
    return __doclensqr__

def getdocurlmap():
    global __docurlmap__
    return __docurlmap__

def geturlqueue():
    global __urlqueue__
    return __urlqueue__

def getqueuedurl():
    global __queuedurl__
    return __queuedurl__

def getsuccesscount():
    global __successcount__
    return __successcount__

def gettotaldispatchedthreadcount():
    global __totalthreaddispatch__
    return __totalthreaddispatch__

'''define locks to global variables'''
urlquelock = threading.Lock()
quedurllock = threading.Lock()
postinglock = threading.Lock()
uniquenumberlock = threading.Lock()

__uniquenumber__ = -1

def generateuniquenumber():
    '''critical section'''
    uniquenumberlock.acquire()
    global __uniquenumber__
    __uniquenumber__ += 1
    uniquenumberlock.release()
    return __uniquenumber__

import re
def litmustesturl(url):
    '''TO DO:
    check if URL is well formed, allowed and satisfies other criteria
    '''

    if settings.__restrictdomain__ and not any(string in url for string in settings.__rooturls__):
        return False
    if any(string in url for string in settings.__badfiletype__):
        return False
    if any(string in url for string in settings.__badurltype__):
        return False
    global __queuedurl__
    global __failedurl__
    #check different versions of same urls
    parturl = re.sub(r'http[s]*://',"",url)
    parturl = re.sub(r'www\.',"",parturl)
    #print("part", parturl, url)
    url1 = "www." + parturl
    url2 = "http://" + parturl
    url3 = "https://" + parturl
    url4 = "http://www."+ parturl
    url5 = "https://www." + parturl

    if url1 in __queuedurl__ or url1 in __failedurl__:
        return False
    if url2 in __queuedurl__ or url2 in __failedurl__:
        return False
    if url3 in __queuedurl__ or url3 in __failedurl__:
        return False
    if url4 in __queuedurl__ or url4 in __failedurl__:
        return False
    if url5 in __queuedurl__ or url5 in __failedurl__:
        return False

    return True
    '''
    if url1 not in __queuedurl__ and url2 not in __queuedurl__ and url3 not in __queuedurl__ \
            and url4 not in __queuedurl__ and url5 not in __queuedurl__ :
        return True
    return False
    '''

jobcondition = threading.Condition()
import urllib.request
def getredirectedurl(myurl):

    url = myurl
    global __queuedurl__
    global __failedurl__
    #if myurl in __queuedurl__:
        #return myurl
    #if myurl in __failedurl__:
        #return myurl
    try:
        response = urllib.request.urlopen(myurl)
        url = response.url.split("#")[0]#remove page anchor character
        url = url.split("?")[0]#remove get parameters
    except Exception as e:
        url = myurl
        __failedurl__[url] = 1
        #print(str(e) + ": " + url)
        logger.writelog(str(e) + ": " + url)
        pass
    finally:
        return url

def enqueueurls(urls,mylevel):
    global __urlqueue__
    global __queuedurl__
    global jobcondition
    with jobcondition:
        try:
            urlquelock.acquire()
            quedurllock.acquire()
            '''critical section'''
            for url in urls:
                url = url.strip("/")
                '''
                get the redirected url if the url redirects.
                you may use original url without obtaining redirected url if needed.
                to do so, comment the statement url = getredirectedurl(url) below.
                '''

                if litmustesturl(url):
                    #print("original ", url)
                    url = getredirectedurl(url)
                    #print("redirected ", url)

                if litmustesturl(url):
                    __urlqueue__.append(str(mylevel) + "#" + url)
                    __queuedurl__[url] = 1
            '''end critical section'''
        except Exception as e:
            logger.writelog(str(e))
            #print(e)
            pass
        finally:
            urlquelock.release()
            quedurllock.release()
            jobcondition.notifyAll()


def dequeueurls(batchsize = 1):
    urlslevels = []
    global __urlqueue__
    global jobcondition
    urlquelock.acquire()
    '''critical section'''
    try:
        for i in range(0,batchsize):
            #print(i)
            if len(__urlqueue__)==0:
                #urlquelock.release()
                break
            urls = __urlqueue__.popleft().split("#")
            urlslevels.append((urls[1], int(urls[0])))

        '''end critical section'''
    except Exception as e:
        pass
    finally:
        urlquelock.release()

    return urlslevels
def updatesuccesscount():
    postinglock.acquire()
    '''critical section'''
    try:
        global __successcount__
        __successcount__ += 1
        #print("hello")
        '''end critical section'''
    except Exception as e:
        pass
    finally:
        postinglock.release()
'''This function is called from urlcrawler's crawlthrough function.
    Since the calculation of length of document should be done after crawling completed,
    the __pushtoposting__ is set to false in settings.py so urlcrawler is not able to call this function for now in this version.
    The setting is set to false because lenght calculation is done only when files are actually downloaded and indexing is done
    offline from collection in this version
'''
def updateposting(text, url):
    postinglock.acquire()
    '''critical section'''
    try:
        global __successcount__
        global __posting__

        logger.writelog("Pushing content of " + url + " in index")
        invertedindex.pushonposting(text.lower(), url, __posting__, __doclensqr__)
        __successcount__ += 1
        #print("hello")
        '''end critical section'''
    except Exception as e:
        pass
    finally:
        postinglock.release()



def pushtobusythreadlist(threadid,thread):
    global ___busythreadlist__
    global __totalthreaddispatch__
    ___busythreadlist__[threadid] = thread
    logger.writelog("Thread " + str(threadid) + " pushed to busy thread list")
    __totalthreaddispatch__ += 1

threadavailablecondition = threading.Condition()
def deletefrombusythreadlist(threadid):

    global ___busythreadlist__
    global threadavailablecondition
    with threadavailablecondition:
        #___busythreadlist__[threadid].join(0)
        del ___busythreadlist__[threadid]
        logger.writelog("Thread " + str(threadid) + " deleted")
        threadavailablecondition.notifyAll()

def setcrawldelay(delay):
    settings.__crawldelay__ = delay

def setmaxthread(numthreads):
    settings.__maxthread__ = numthreads

def setcrawldepth(depth):
    settings.__crawldepth__ = depth

def setminpagesize(wordcount):
    settings.__minwordinpage__ = wordcount

def getminpagesize():
    return settings.__minwordinpage__

def setverbosity(verbosity):
    if verbosity == "true":
        settings.__verbose__ = True
    if verbosity == "false":
        settings.__verbose__ = False

def getcrawldepth():
    return settings.__crawldepth__
def getcrawldelay():
    return settings.__crawldelay__
def getmaxthread():
    return settings.__maxthread__
def getcrawldelay():
    return settings.__crawldelay__

def getmaxjobsize():
    return settings.__maxjobsize__

def setmaxjobsize(size):
    settings.__maxjobsize__ = size

def setsaverawtext(truefalse):
    settings.__saverawpage__ = truefalse
def issaverawtext():
    return settings.__saverawpage__
def pushtoposting():
    return settings.__pushtoposting__
def setpushtoposting(truefalse):
    settings.__pushtoposting__ = truefalse