#__author__ = 'dipesh'
__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''

from resources import settings
from crawler import globals
from indexer import invertedindex
from searchengine import queryhandler
import time
print("search engine")

print("Indexing")

t1 = time.time()
invertedindex.createinvertedindex(settings.__preprocessed_dir__, postinglist=globals.getposting(),
                                  doclensqrlist=globals.getdoclensqrlist(),docurlmap=globals.getdocurlmap())

t2 = time.time()
print("Indexing completed in ", t2-t1, " secs")

queryhandler.runserver("localhost", 80,globals.getposting(),globals.getdoclensqrlist(),
                       settings.__searchpagetemplate__,globals.getdocurlmap())


