#__author__ = 'dipesh'
from lib import tokengenerator

__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''

'''
parameters: textfile = path of text file,
            tolower = a boolean flag; flag = True indicates convert text to lower before processing
return: statistics as dictionary;
three statistics viz. count of totalwords, uniquewords and wordfrequency; word and frequency pairs in the file.
 '''


def generatewordstatisticsintext(text, tolower = True):

    mytext = text.split("\n")
    wordstatistics = {"totalwords":0, "vocabularysize":0, "wordfrequency":{}}
    for line in mytext:
        if tolower:
            line = line.lower()
        #words = line.strip("\n").split(" ")
        words = tokengenerator.gettokens(line)
        for word in words:
            wordstatistics['totalwords'] += 1
            if word in wordstatistics['wordfrequency']:
                wordstatistics['wordfrequency'][word] += 1
            else:
                 wordstatistics['wordfrequency'][word] = 1
    wordstatistics["vocabularysize"] = len(wordstatistics['wordfrequency'])
    return wordstatistics


def generatewordstatisticsinfile(textfile,tolower=True):
    myfile = open(textfile)

    wordstatistics = {"totalwords":0, "vocabularysize":0, "wordfrequency":{}}
    for line in myfile:
        if tolower:
            line = line.lower()

        words = tokengenerator.gettokens(line)
        for word in words:
            wordstatistics['totalwords'] += 1
            if word in wordstatistics['wordfrequency']:
                wordstatistics['wordfrequency'][word] += 1
            else:
                 wordstatistics['wordfrequency'][word] = 1
    myfile.close()
    wordstatistics["vocabularysize"] = len(wordstatistics['wordfrequency'])
    return wordstatistics
