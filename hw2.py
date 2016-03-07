#__author__ = 'dipesh'
__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''
import sys
from fileprocessor import wordstatisticsgenerator, linetolinefilecopier
from lib import dictionaryprocessor
sourcefile = None
destinationfile = None
if len(sys.argv) >1:
    sourcefile = sys.argv[1]
if len(sys.argv) >2:
    destinationfile = sys.argv[2]

if sourcefile == None or destinationfile == None:
    print("Source file (and/or) destination file not supplied; program used default filenames for those")

if sourcefile == None:
    sourcefile = "documents/Information Retrieval at Institute for Intelligent Systems_The University of Memphis.txt"
if destinationfile == None:
    destinationfile = "documents/copy_ir-websearch.txt"


print("------------------Copying source file to destination line by line------------------" )
linetolinefilecopier.copyfile(sourcefile,destinationfile,True)#True means copy line by line
input("Done copying!\nPress any key to continue")
print("------------------Generating word stantistics------------------")
stats = wordstatisticsgenerator.generatewordstatisticsinfile(destinationfile)

pairs = dictionaryprocessor.sortdictionarybykey(stats['wordfrequency'])
print("Total words: "+str(stats['totalwords']), "Vocabulary size: "+ str(stats['vocabularysize']))
input("Continue----")
for k, v in pairs:
    print(k,v)

#from fileprocessor import webpagesaver

#webpagesaver.savewebpage("http://www.cs.memphis.edu/~vrus/teaching/ir-websearch", "documents/ir-websearch.txt",True)