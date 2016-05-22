# encoding=utf8
import sys, json, urllib, urllib2, base64, logging
from BeautifulSoup import *

commonRequestParams = {
}

def parseHtml(html, soupAttrs, parser, output={}):
    soup = BeautifulSoup(html)
    return reduce(parser, soup.findAll(**soupAttrs), output)
    

def httpGet(url, data={}, headers={}):
    newData = commonRequestParams.copy()
    newData.update(data)
    headers.update({"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36"})
    request = urllib2.Request(url + "?" + urllib.urlencode(newData), None, headers)
    response = urllib2.urlopen(request)
    return response.read()

def printJson(data, out=sys.stdout):
    out.write(json.dumps(data) + "\n")

def loadResource(pathname_suffix):
    cands = [os.path.join(d, pathname_suffix) for d in sys.path]
    try:
        return filter(os.path.exists, cands)[0]
    except IndexError:
        return None
