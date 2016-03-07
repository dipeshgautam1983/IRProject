__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''

#myurl ="http://www.orimi.com/pdf-test.pdf"
#myurl = "http://www.cs.memphis.edu/~vrus/teaching/ir-websearch"
#myurl = "http://web0.cs.memphis.edu/~vrus//teaching/ir-websearch/assignments/assignment-02.txt"
#myurl = "http://web0.cs.memphis.edu/~vrus//teaching/ir-websearch/lectures/IR.textCategorization-2.session-17.ppt"
myurl = "http://web0.cs.memphis.edu/~vrus//teaching/ir-websearch/"
#myurl = "http://web0.cs.memphis.edu/~vrus//teaching/ir-websearch/lectures/IR.webCrawling.extraSlides.ppt"
#myurl = "http://tartarus.org/~martin/PorterStemmer/"
#myurl = "http://www.ecdevelopment.org/wp-content/uploads/2015/04/hippie-flower.jpg"
#myurl = "http://www.cs.memphis.edu/~vrus/teaching/ir-websearch/papers/codingStyle.html"
#myurl = "http://web0.cs.memphis.edu/~vrus//teaching/ir-websearch/papers/mapReduce.pdf"
myurl = "http://www.memphis.edu/"
#myurl = "http://www.ioe.edu.np"
#myurl = "http://www.memphis.edu/academics/colleges-schools.php"
#myurl = "https://podcasts.memphis.edu"
#myurl = "http://www.gotigersgo.com"
import threading

from resources import settings
from crawler import globals
from crawler import threadmanager,uimanager
from indexer import invertedindex
from lib import textpreprocessor


#urlcrawler.crawlthrough([myurl],1,settings.__outputdir__)


print("HW6")
userinput = input('enter "1" for preprocessing or "2" for indexing or "3" for crawling: ')
if userinput.lower() == "1":
    print(".............preprocessing............")
    textpreprocessor.preprocesscollection(srcfolder=settings.__outputdir__, destfolder = settings.__preprocessed_dir__)
    print("preprocessing completed")
elif userinput.lower() == "2":
    print(".............creating inverted index............")
    invertedindex.createinvertedindex(settings.__preprocessed_dir__, postinglist=globals.getposting(),
                                      doclensqrlist=globals.getdoclensqrlist(),docurlmap=globals.getdocurlmap())
    '''dump posting to file'''
    mydumpfile = open("postdump.txt","w")
    for token in globals.getposting():
        line = ""
        tf, doclist = globals.getposting()[token]
        line += token + " " + str(tf)
        for docid in doclist:
            df = doclist[docid]
            line += " " + docid + " " + str(df)
        mydumpfile.write(line+"\n")
        mydumpfile.flush()
    mydumpfile.close()


    #print(globals.getposting())

elif userinput.lower() == "3":
    print(".............crawling....................")
    crawlerthread = threading.Thread(target=threadmanager.assignjobs, args = ([myurl],settings.__crawldepth__,settings.__outputdir__,settings.__maxthread__) )
    uithread = threading.Thread(target = uimanager.commandhandler)
    crawlerthread.start()
    uithread.start()
else:
    print("You did not give valid command.\n  Try again later.\n    Bye")
    exit(0)
