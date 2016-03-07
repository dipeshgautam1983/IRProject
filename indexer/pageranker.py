#__author__ = 'dipesh'
__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''

#import os
import re
import math
from lib import textpreprocessor
'''
def getrankedlist(query, pages=[]):


    return query
'''
'''
def computesimilarity(query,text):
    similarity = 0.0
    return similarity
'''

def getrankeddocumentlist(invertedindex, query="", doclensqrlist={}):

    query = query.lower()
    '''preprocess query'''
    query = textpreprocessor.preprocess(query)
    query = re.sub(r"[ \t]+"," ", query)
    qtokens = query.split(" ")
    keywordlist = {}
    numdocs = len(doclensqrlist)

    for token in qtokens:
        if token in keywordlist:
            keywordlist[token] += 1
        else:
            keywordlist[token] = 1

    #df, doclistwithmytoken = postinglist[mytoken]

    #calculate partial product for each token in query and document that contain the tokens
    #the sum of partial product gives dot product of query and the document
    # to calculate, iterate through each query term and through each document that contains query term
    lenqsqr = 0.0
    retrieveddocs = {}
    for token in keywordlist:
        if token not in invertedindex:
            continue

        #print(token)
        tfq = keywordlist[token]
        #print(tfq)
        df,docswithtoken  = invertedindex[token]
        idf = math.log(numdocs/df,2) #idf of token in query
        #print(numdocs, df)
        wq = tfq * idf # weight of token in query
        lenqsqr += wq * wq
        for document in docswithtoken:
            tfd = docswithtoken[document]
            wd = tfd * idf # weight of token in document
            if document not in retrieveddocs:
                retrieveddocs[document] = 0.0

            retrieveddocs[document] += wq*wd #partial product of component of query and document vector for dot product

    list = []
    '''remove documents with zero scores and calculate normalized score for others'''
    for doc in retrieveddocs:
        if retrieveddocs[doc] > 0:
            rankscore = retrieveddocs[doc] /(math.sqrt(lenqsqr * doclensqrlist[doc]))
            list.append((doc,rankscore))

    ranked = sorted(list, key = lambda x:x[1],reverse=True)
    return ranked



'''
def getrankedlist(query, pagefolder):

    inputfiles = os.listdir(pagefolder)
    for file in inputfiles:
        filename = pagefolder.strip("/") + "/" + file
        inputfile = open(filename, "r")


        inputfile.close()
    return inputfiles

'''


#print(getrankeddocumentlist("test query", "../documents"))
