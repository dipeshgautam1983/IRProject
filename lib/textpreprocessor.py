#__author__ = 'dipesh'
__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''
from nltk.stem.porter import *
from nltk import word_tokenize
from resources import settings
import re
import os
import io
import string
def dostemming(text):
    stemmer = PorterStemmer()
    tokens = text.split(" ")
    stemmed = [stemmer.stem(token) for token in tokens]
    return " ".join(stemmed)

def removestopwords(text):
    txtarr = word_tokenize(text)
    refined = ""
    #print(settings.__stoplist__)
    for txt in txtarr:

        if txt not in settings.__stoplist__:
            #print(txt)
            refined += txt + " "
    return refined.strip(" ")

def dofinalprocessing(text):
    text = re.sub(r"[0-9]+","",text)
    words = text.split()
    refined = ""
    for word in words:
        if word not in settings.__stoplist__ and len(word)>2:
            refined += word + " "
    return refined.strip(" ")

def removepunctuations(text):
    text = re.sub(r"["+string.punctuation+"]"," ", text)
    tokens = word_tokenize(text)
    return " ".join(tokens)

def removeurls(text):
    text = re.sub(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\']))', ' ', text)
    return text

def dolemmatization(text):
    return text
def preprocess(text):
    txt = text
    #txt = removeurls(text)
    #print(text)
    txt = removestopwords(txt)
    txt = removepunctuations(txt)
    txt = dostemming(txt)
    txt = dolemmatization(txt)
    txt = dofinalprocessing(txt)
    return txt

def preprocesscollection(srcfolder, destfolder ):
    inputfiles = os.listdir(srcfolder)
    if len(inputfiles) <=0:
        print("No files in source folder\Please try again later\nBye!!")
        return
    print('Processing files in "' + srcfolder +'" folder')
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

        body = preprocess(body)
        filename,extension = os.path.splitext(inputfile)
        dfile = open(destfolder.strip("/") + "/" + filename + ".processed" + extension,'w',encoding="utf8")
        dfile.write(header)
        dfile.write("\n")
        dfile.write(body)
        dfile.flush()
        dfile.close()
        ipfile.close()

    print('Processed files are written in "' + destfolder +'" folder')
