#__author__ = 'dipesh'
__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''

import threading
import time
__count__ = 0
threadlock = threading.Lock()
# Define a function for the thread
def print_time( threadName, delay):
    #count = 0
    global __count__

    while __count__ < 5:
        threadlock.acquire()
        __count__ += 1
        time.sleep(delay)
        print("%s: %s" % ( threadName, time.ctime(time.time()) ),__count__)
        threadlock.release()

# Create two threads as follows
try:
    t1 = threading.Thread( target = print_time, args = ("Thread-1", 4, ))
    t1.start( )
    t1 = threading.Thread( target = print_time, args = ("Thread-2", 4, ))
    t1.start( )
except Exception as e:
    print(e,"Error: unable to start thread")

print("main completed")
exit(0)
'''
while 1:
    print("pass")
    time.sleep(5)
    pass
'''