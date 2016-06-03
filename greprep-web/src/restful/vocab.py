import webapp2, logging
from google.appengine.api import memcache
from words.dictref import *

class VocabListResourceHandler(webapp2.RequestHandler):
    
    def get(self):
        offset = numerize(self.request.get("o"), 0)
        length = numerize(self.request.get("l"), 10)
        sortKey = self.request.get("s", default_value="word")
        listKey = "def:vocab-list:%d:%d:%s" % (offset, length, sortKey)
        logging.info("listKey=%s" % listKey)
        
        defs = memcache.get(listKey)
        if defs is None:
            with open("data/majortests.json") as f:
                defs = json.load(f)
                
            def toMap(k):
                return {
                    "word": k,
                    "definition": defs.get(k)
                }
            defs = sorted([toMap(k) for k in defs.keys()], key=lambda k: k[sortKey])
            memcache.add(listKey, defs, 86400 * 15)
        
        return webapp2.Response(json.dumps(defs[offset:(offset+length)]))

    def delete(self):
        logging.info("HTTP Delete called")
        pass

class VocabResourceHandler(webapp2.RequestHandler):
    
    def get(self, word):
        logging.info("Looking up the word: " + word)
        
        wordDef = memcache.get("def:%s" % word)
        if wordDef is None:
            logging.info("[CACHE-MISS] Loading word '%s'" % word)
            wordDef = webapp2.Response(json.dumps(lookupDictionaryCom(word)))
            memcache.add("def:%s" % word, wordDef, 86400 * 15)

        return wordDef
    