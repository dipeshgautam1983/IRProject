#__author__ = 'dipesh'
__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''

'''
parameters: worddictionary = a dictionary of word and frequency; key as words,
return: list of word frequency pair sorted in alphabetical order
 '''
def sortdictionarybykey(worddictionary):
    pair = [(k,v) for k, v in worddictionary.items()]
    pair.sort()
    return pair
