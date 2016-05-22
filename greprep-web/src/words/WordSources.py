import sys, json, re
from commons import *

def majorTestsWordsCollector():
    def majorTestsWordParser(words, item):
        if item is None: return
        
        words.update({row.find("th").next: 
                      reduce(lambda contents, text: contents + str(text), row.find("td"), "").strip("\r\n ") 
                      for row in item.findAll("tr")})
        return words
    
    def fetchWords(idx):
        url = "http://www.majortests.com/gre/wordlist_%02d" % idx
        return parseHtml(httpGet(url),
                     {
                      "attrs": {"class": re.compile("wordlist")}
                      },
                     majorTestsWordParser)
    
    allWords = {}
    for x in range(1, 16):
        allWords.update(fetchWords(x))
    return allWords
    
if __name__ == "__main__":
    print json.dumps(majorTestsWordsCollector())
    
    
