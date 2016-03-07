#__author__ = 'dipesh'
__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''
from resources import settings
import datetime
import threading
filelock = threading.Lock()
def writelog(message):

    message = str(message)
    if settings.__verbose__:
        print(message)
    '''write log with date and time'''
    nowtime = datetime.datetime.now()
    timestr = str(nowtime)
    logfilename = timestr.split(" ")[0]
    logfilename = logfilename.replace("-","_")

    try:
        '''critical section'''
        global filelock
        filelock.acquire()
        logfile = open(settings.__logdir__ + "/" + logfilename + ".txt","a")
        logfile.write(timestr+ "\t" + message)
        logfile.write("\r\n")
        logfile.flush()
        logfile.close()

    except Exception as e:
        pass
    finally:
        filelock.release()