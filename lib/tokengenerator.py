#__author__ = 'dipesh'
import re

__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''

def gettokens(text):
    return re.compile('\w+').findall(text)