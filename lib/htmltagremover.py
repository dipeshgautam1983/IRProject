#__author__ = 'dipesh'
__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''

from bs4 import BeautifulSoup
def removetags(text):
    soup = BeautifulSoup(text,"html.parser")
    return soup.get_text()
