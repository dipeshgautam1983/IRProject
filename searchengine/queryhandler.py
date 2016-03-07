__author__ = 'Dipesh Gautam' \
             'email: dgautam@memphis.edu'
'''---------------------------------------------------'''

from http.server import BaseHTTPRequestHandler,HTTPServer
from indexer import pageranker
import re
import time
import urllib

class QueryHandler(BaseHTTPRequestHandler):
    Postings = None
    DocLenSqrList = None
    PageTemplate = None
    DocUrlMap = None
    def setvariables(self, postings, doclensqrlist, pagetemplate, docurlmap):
        self.Postings = postings
        self.DocLenSqrList = doclensqrlist
        self.PageTemplate = pagetemplate
        self.DocUrlMap = docurlmap

    def getpage(self, query=""):

        query = urllib.parse.unquote(query)
        print(self.client_address, " sent query: " , query)
        f = open(self.PageTemplate)
        template = f.read()
        f.close()
        if query == "":
            return re.sub(r'<!-- #Search Result here -->', " ", template)

        query = re.sub(r'[+]+',' ',query)

        t1 = time.time()
        list = pageranker.getrankeddocumentlist(self.Postings,query,self.DocLenSqrList)
        t2 = time.time()
        result = "<p>" + str(len(list)) + " document(s) retrieved for query: <b>" + query + "</b> in " + str(t2-t1) + " secs</p>"
        count = 0
        for page, rank in list:
            count += 1
            result += '\n<p>' + str(count) + '. [' + page + '] <a href="' + self.DocUrlMap[page][0] + '"target="_blank">' + self.DocUrlMap[page][0] + '</a>\t[' + str(rank) + ']</p>'

        #append search result with template to build content
        content = re.sub(r'<!-- #Search Result here -->', result, template)

        return content

    def do_HEAD(self):
        #print(self.headers)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        content = ""
        try:
            if self.path == "/":
                content = self.getpage()
                #print(content)
            elif self.path.startswith("/?query="):
                query = self.path.split("/?query=")[1]
                content = self.getpage(query)

            else:
                self.send_error(404, "Page not found")
                return

            #print("out "+content)
            #send code 200
            self.send_response(200)
            #send header
            self.send_header('Content-type','text-html')
            self.end_headers()
            #send file content
            self.wfile.write(bytes(content, 'UTF-8'))
            return

        except IOError:
            self.send_error(404, "Page not found")

    def do_POST(self):
        try:
            postvarlen = int(self.headers['Content-Length'])
            postvars = self.rfile.read(postvarlen)
            querystr = postvars.decode('UTF-8').split("query=")[1]
            query = querystr.split("&")[0]
            content = self.getpage(query)
            self.wfile.write(bytes(content, "UTF-8"))

        except IOError:
            self.send_error(404, "Page not found")


def runserver(host, port,postings,doclensqrlist,pagetemplate,docurlmap):
    print('http server is starting...')
    server_address = (host, port)
    QueryHandler.setvariables(QueryHandler,postings,doclensqrlist,pagetemplate,docurlmap)
    httpd = HTTPServer(server_address, QueryHandler)
    print('http server is running...')
    httpd.serve_forever()


