#__author__ = 'dipesh'
__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''

import collections

from bs4 import BeautifulSoup
import re

'''this functions returns www.google.com/flights when supplied www.google.com/flights/index.htm'''
def getabsoluteurl(sourceurl,extractedlink):

    '''
    www.google.com/flights
    www.google.com
    http://www.google.com/flights
    http://www.google.com
    http://www.google.com/flights
    http://www.google.com/flights/index.htm"
    '''


    url = extractedlink.split("#")[0]#remove page anchor character
    url = url.split("?")[0]#remove get parameters


    if "index." in url:
        url = url.split("index.")[0].rstrip("/")
        #url = url.strip(url.split("/")[-1])

    '''
    if extractedlink == "http://www.memphis.edu/umtech/service_desk/index.php":
        print("EXTRACTEDDDDDD",url,"splits ", url.split("/"),"first", url.split("/")[-1])
    '''
    if (url.startswith('http://') or url.startswith('https://') or  url.startswith('www.')):
        return url.rstrip("/")

    if sourceurl == "":
        return url.rstrip("/")

    sourceurl = sourceurl.rstrip("/")
    parent = sourceurl
    currenturlparts = sourceurl.split("//")#[http:, www.google.com/flights/abc.php]
    parentparts = currenturlparts[-1].split("/")# [www.google.com, flights, abc.php] currenturlparts[-1] = www.google.com/flights/abc.php and split further and take first to get root
    root = parentparts[0] #www.google.com
    '''obtain root url '''
    if len(currenturlparts) > 1: #append http: part infront
        root = (currenturlparts[0] + "//" + root).rstrip("/")
    '''obtain parent url'''
    if len(parentparts) > 1: #if [www.google.com, flights, abc.php]
        if "." in parentparts[-1]:
            parent = re.sub(r''+parentparts[-1].strip("/"),"",parent)
            #parent = parent.strip(parentparts[-1]).strip("/")

    '''construct absolute urls either by root or parent'''
    if url.startswith("/"):
        url = root + "/" + url.strip("/")
        return url.strip("/")

    url = parent + "/" + url.strip("/")
    return url


def fetchurls(rawhtmltext, sourceurl = "", soup = None):

    if soup == None:
        soup = BeautifulSoup(rawhtmltext,"html.parser")

    uniqueurl = collections.OrderedDict()
    for anchor in soup.findAll('a', href=True):
        link = anchor['href']
        uniqueurl[getabsoluteurl(sourceurl,link)] = 1
    return uniqueurl
'''
def getcleantext(rawhtmltext, soup = None):
    if soup == None:
        soup = BeautifulSoup(rawhtmltext,"html.parser")
    return soup.getText()
    for dirty in soup(["script","style"]):
        dirty.extract()  #remove java scripts and styles
    return soup.get_text()
'''

def getcleantext(rawhtmltext):

    #print(rawhtmltext)
    # remove javascript or css
    cleantext = re.sub(r"(?is)<(script|style).*?>.*?(</\1>)", "", rawhtmltext.strip())
    # remove html comments. This has to be done before removing regular
    # tags since comments can contain '>' characters.
    cleantext = re.sub(r"(?s)<!--(.*?)-->[\n]?", "", cleantext)
    # remove the remaining tags:
    cleantext = re.sub(r"(?s)<.*?>", " ", cleantext)
    # remove whitespaces
    cleantext = re.sub(r"&nbsp;", " ", cleantext)
    #cleantext = re.sub(r"  ", " ", cleantext)
    #cleantext = re.sub(r"  ", " ", cleantext)
    #remove urls in text
    cleantext = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', ' ', cleantext)#remove http://
    cleantext = re.sub(r'www(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*',' ',cleantext)#remove www.
    #remove whitespaces
    cleantext = re.sub(r'[ \n\r\t]+'," ",cleantext)
    return cleantext.strip()

def getcleantextandurls(rawhtmltext,sourceurl = ""):

    soup = BeautifulSoup(rawhtmltext,"html.parser")
    uniqueurl = fetchurls(rawhtmltext,sourceurl,soup)
    '''
    if "https://podcasts.memphis.edu/ttp://www.memphis.edu/umtech/service_desk" in uniqueurl:
        print("\n\n\n",sourceurl,"\n*************\n", list(uniqueurl.keys()))
    '''
    '''
    print("**********************")
    print(sourceurl, ":\n", list(uniqueurl.keys()))
    print("**********************")
    '''
    #soup.prettify()
    return list(uniqueurl.keys()),getcleantext(rawhtmltext)


from lib import urlcontentreader

'''
def fetchurlandtext(sourceurl,makeabsoluteurl=True):

    rawtext = urlcontentreader.readtextfromurl(sourceurl)
    if makeabsoluteurl:
        urls , text = getcleantextandurls(rawtext,sourceurl)
        #print(urls)
        return urls, text
    urls, text = getcleantextandurls(rawtext)

    return urls, text
'''