#__author__ = 'dipesh'
__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''
from crawler import globals
from resources import settings
commandlist = ["setdelay", "setmaxthread", "setcrawldepth","setminpagesize","verbose", "pause", "stop","quit" "status", "viewlog"]
def crawlsummary():
    print("To be done")
def verbose():
    print("To be done")
def parsecommandandparms(userinput):
    splt = userinput.split()
    cmd = ""
    parm = ""
    if len(splt) > 0:
        cmd = splt[0]
    if len(splt)>1:
        parm = splt[1]
    return (cmd,parm)

def printsummary():

    print("Crawl depth: ", globals.getcrawldepth())
    print("Crawl delay: ", globals.getcrawldelay())
    print("Max thread: ", globals.getmaxthread())
    print("Total thread dispatched so far: ", globals.gettotaldispatchedthreadcount())
    print("Total active threads: ", len(globals.getbusythreadlist()))
    print("Total pages queued so far: ", len(globals.getqueuedurl()))
    print("Total pages attempted to crawled so far: ", len(globals.getqueuedurl())-len(globals.geturlqueue()))
    print("Total pending pages to crawl: ", len(globals.geturlqueue()))
    print("Total number of pages successfully crawled: ", globals.getsuccesscount())

def commandhandler():

    userinput = input("MyCrawler->> ")
    cmd,parm = parsecommandandparms(userinput.lower())
    while cmd != "quit":

        if cmd == "setdelay":
            if not parm.isdigit():
                print("Parameter missing or parameter not a positive integer")
            else:
                globals.setcrawldelay(int(parm))
        elif cmd == "setmaxthread":
            if not parm.isdigit():
                print("Parameter missing or parameter not a positive integer")
            else:
                globals.setmaxthread(int(parm))

        elif cmd == "setcrawldepth":
            if not parm.isdigit():
                print("Parameter missing or parameter not a positive integer")
            else:
                globals.setcrawldepth(int(parm))
        elif cmd == "setminpagesize":
            if not parm.isdigit():
                print("Parameter missing or parameter not a positive integer")
            else:
                globals.setminpagesize(int(parm))

        elif cmd == "verbose":
            if parm != "true" and parm != "false" and parm != "t" and parm != "f":
                print("Parameter missing or parameter not equals t[rue] or f[alse]")
            else:
                if parm == "t":
                    param = "true"
                if parm == "f":
                    parm = "false"
                globals.setverbosity(parm)

        elif cmd == "":
            pass

        elif cmd == "pause":
            print("This command is not implemented in this version")

        elif cmd == "stop":
            print("This command is not implemented in this version")

        elif cmd == "quit":
            pass

        elif cmd == "status":
            printsummary()

        elif cmd == "viewlog":
            print("This command is not implemented in this version")


        userinput = input("MyCrawler->> ")
        cmd, parm = cmd,parm = parsecommandandparms(userinput.lower())

    if cmd == "quit":
        '''
        threadlist = list(globals.getbusythreadlist())
        for busythread in globals.getbusythreadlist():
            globals.getbusythreadlist()[busythread].join(0)
            #del globals.getbusythreadlist()[busythread]
        exit(0)
        '''
        print("BYE!!")

    '''

    userinput = ""
    while userinput != "quit":
        userinput = input("MyCrawler->> ").lower()
        if userinput == "quit":
            print("BYE!!")
        elif userinput == "setdelay":

            print("delay")
    '''
'''
posting = globals.getposting()
print("\n\n--------------Summary---------------\n\n")
print("WORD\t\t\t\tDOC_FREQ\t\t\tDOCUMENT AND TERM FREQ")
for post in posting:
        try:
            print(u""+str(post), len(posting[post]),posting[post])
        except Exception:
            pass




 userinput = ""
    cmd,parm = ("","")#parsecommandandparms(userinput)
    while cmd != "quit" in (cmd,parm) in  parsecommandandparms(userinput):

        if cmd == "quit":
            print("BYE!!")
        elif cmd == "setdelay":

            print("delay")
        userinput = input("MyCrawler->> ")

'''