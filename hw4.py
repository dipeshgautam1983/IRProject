#__author__ = 'dipesh'
__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''

from resources import settings
from lib import textpreprocessor
from resources import settings

import os
import time
filelist = [ f for f in os.listdir(settings.__preprocessed_dir__) ]
for f in filelist:
    os.remove(settings.__preprocessed_dir__ + "/" + f)

#time.sleep(10)

print("hw4")



textpreprocessor.preprocesscollection(srcfolder=settings.__outputdir__, destfolder = settings.__preprocessed_dir__)

print("Preprocessing completed")
