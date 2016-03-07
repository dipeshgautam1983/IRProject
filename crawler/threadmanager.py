#__author__ = 'dipesh'
__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''
from crawler import globals
from crawler import urlcrawler
import time
import threading
def getbatchsize(jobqueue,availablethread):
    totaljobs = len(jobqueue)
    if len(jobqueue)==0:
        return 0
    numofthreads = availablethread
    if totaljobs < availablethread:
        numofthreads = totaljobs
    #print ("jobs, numthreads",totaljobs,numofthreads)
    batchsize = int(totaljobs/numofthreads)
    return batchsize

def getjobsize():
    return min(globals.getmaxjobsize(),len(globals.geturlqueue()))

def assignjobs(seedurls, crawlingdepth, outputdir, maxthread = 1):
    '''enque seed urls'''
    mylevel = 0 #level of seedurl is root level
    globals.enqueueurls(seedurls,mylevel)

    threadid = -1
    while len(globals.geturlqueue())>0 or len(globals.getbusythreadlist())>0:

        with globals.jobcondition:
            if len(globals.geturlqueue()) == 0: ##if no job in queue
                globals.jobcondition.wait()

        with globals.threadavailablecondition:
            if len(globals.getbusythreadlist()) == globals.getmaxthread(): ##if all threads are busy
                globals.threadavailablecondition.wait()

        ''' get the job of jobsize '''
        urlslevels = globals.dequeueurls(getjobsize())
        threadid += 1
        crawlingdepth = globals.getcrawldepth()
        '''assign jobs to threads'''
        thread = threading.Thread(target = urlcrawler.crawlthrough, args = (urlslevels,crawlingdepth, threadid, outputdir))
        globals.pushtobusythreadlist(threadid,thread)
        thread.start()

