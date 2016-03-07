#__author__ = 'dipesh'


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
from crawler import urlcrawler
from resources import settings
from crawler import globals
from crawler import threadmanager
#urlcrawler.crawlthrough([myurl],1,settings.__outputdir__)
threadmanager.assignjobs([myurl],1,settings.__outputdir__,1)
posting = globals.getposting()
print("\n\n--------------Summary---------------\n\n")
print("WORD\t\t\t\tDOC_FREQ\t\t\tDOCUMENT AND TERM FREQ")
for post in posting:
        try:
            print(u""+str(post), len(posting[post]),posting[post])
        except Exception:
            pass
