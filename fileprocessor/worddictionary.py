#__author__ = 'dipesh'
__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''

'''
parameters: textfile = path of text file,
            tolower = a boolean flag; flag = True indicates convert text to lower before processing
return: word and frequency as dictionary
 '''
def getworddictionary(textfile, tolower = True):
    myfile = open(textfile)
    worddictionary = {}
    for line in myfile:
        if tolower:
            line = line.lower()
        words = line.strip("\n").split(" ")
        for word in words:
            if word in worddictionary:
                worddictionary[word] += 1
            else:
                worddictionary[word] = 1
    myfile.close()
    return worddictionary

