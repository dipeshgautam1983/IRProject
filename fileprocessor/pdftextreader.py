#__author__ = 'dipesh'
__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''

from PyPDF2 import PdfFileWriter, PdfFileReader

def readpdftext(path):

    # Load pdf file into PyPDF2
    pdffile = open(path, "rb")
    pdfreader = PdfFileReader(pdffile)
    # Iterate through each page
    pagecontent = ""
    for i in range(0, pdfreader.getNumPages()):
        # Extract text from page and add to content
        pagecontent += pdfreader.getPage(i).extractText() + "\n"
    # Collapse whitespace
    pagecontent = " ".join(pagecontent.replace(u"\xa0", " ").strip().split())
    pdffile.close()
    return pagecontent
