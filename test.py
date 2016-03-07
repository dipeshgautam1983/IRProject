#__author__ = 'dipesh'
__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''


'''
from lib import webpagereader

#url = "https://podcasts.memphis.edu//ttp://www.memphis.edu/umtech/teaching/ttp://www.memphis.edu/notice/ttp://www.memphis.edu/umtech/service_desk"
url = "https://podcasts.memphis.edu"
#url = "http://www.memphis.edu"
text = webpagereader.readhtmlpage(url,False)

print(text)
'''
import os
import io
import time
dir = "preprocessed_docs"
files = os.listdir(dir)
worddict = {}

t1 = time.time()

for file in files:
    fn = dir + "/" + file
    f = open(fn)
    for line in f:
        splts = line.split()
        for word in splts:
            worddict[word] = 1
        #print(line)
    f.close()
t2 = time.time()

print("time ", t2-t1, len(worddict))

files = os.listdir(dir)
worddict = {}


from lib import tokengenerator
t1 = time.time()

for file in files:

    fn = dir + "/" + file
    f = io.open(fn,'r',encoding="utf8",errors='ignore')
    txt = f.read()
    tokens = tokengenerator.gettokens(txt)
    #splts = txt.split()
    for token in tokens:
        worddict[token] = 1

    f.close()

t2 = time.time()

print("time ", t2-t1, len(worddict))