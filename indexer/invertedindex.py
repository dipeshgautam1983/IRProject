#__author__ = 'dipesh'
__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''

from lib import tokengenerator
import math
def pushonposting(text, docid, postinglist=None, doclensqrlist = None):
    
    if postinglist == None:
        postinglist={}
    if doclensqrlist == None:
        doclensqrlist = {}
    
    tokens = tokengenerator.gettokens(text)

    '''create inverted index'''
    for mytoken in tokens:
        mytoken = str.lower(mytoken)
        if mytoken in postinglist:
            df, doclistwithmytoken = postinglist[mytoken]
            if docid in doclistwithmytoken:
                tf = doclistwithmytoken[docid]
            else:#add new document
                tf = 0
                df +=1
            #increment tf
            doclistwithmytoken[docid] = tf + 1
            postinglist[mytoken] = (df, doclistwithmytoken)
        else: #else add new token and new document to posting and update tf of docid to 1
            doclistwithmytoken = {docid:1}
            postinglist[mytoken] = (1, doclistwithmytoken)# first entry of tuple is df
        #print(token)
    #print(postinglist)

def calculatedocumentvectorlengths(postinglist, doclensqrlist):

    '''create document vector length square list'''
    numdocs = len(doclensqrlist)

    for token in postinglist:
        df, doclistwithmytoken = postinglist[token] # postinglist values are tuples of df and another hash

        idf = math.log(numdocs/df,2)
        if idf == 0:
            continue
        ''''''
        for doc in doclistwithmytoken:
            tf = doclistwithmytoken[doc]
            tfidf = tf * idf
            doclensqrlist[doc] += tfidf*tfidf




    #text = "HELLO"
import os
import io
import re
def createinvertedindex(srcfolder, postinglist=None, doclensqrlist=None, docurlmap = None):
    
    if postinglist == None:
        postinglist = {}
    if doclensqrlist == None
        doclensqrlist = {}
    if docurlmap == None
        docurlmap = {}
    
    inputfiles = os.listdir(srcfolder)
    if len(inputfiles) <= 0:
        print("No files in source directory\nPlease try again later\nBye!!")
        return
    print('Indexing files in "' + srcfolder +'" folder')

    '''initialize documentlengthlist'''
    for inputfile in inputfiles:
        docid = inputfile.split("/")[-1]
        doclensqrlist[docid] = 0.0

    count = 0
    for inputfile in inputfiles:
        #print("processing " +  inputfile)
        ipfile = io.open(srcfolder.strip("/") + "/" + inputfile,'r',encoding="utf8",errors='ignore')
        text = ipfile.read()

        '''Extract header'''
        start = text.find('#') + 1
        end = text.find("\n",start)
        header = text[start:end]
        '''extract body by removing header'''
        body = re.sub("#(.*)\n","",text).lower()
        #docid = re.sub("[\r\n]+","",header).strip()
        docid = inputfile.split("/")[-1]

        pushonposting(body, docid, postinglist,doclensqrlist)
        '''map files saved with corresponding urls'''
        docurlmap[docid] = [header]

        ipfile.close()
        count+=1
        #print(docid," ", count, " pushed in posting")
    calculatedocumentvectorlengths(postinglist, doclensqrlist)
    print('Total ' + str(len(postinglist)) + " words from " + str(count) + ' files in "'+ srcfolder+'" successfully indexed')