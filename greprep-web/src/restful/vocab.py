import webapp2, logging
from google.appengine.api import memcache
from words.dictref import *

class VocabListResourceHandler(webapp2.RequestHandler):
    def get(self, offset=0, length=10):
        defs = memcache.get("def:vocab-list")
        if defs is None:
            with open("data/majortests.json") as f:
                defs = json.load(f)
                
            def toMap(k):
                return {
                    "word": k,
                    "definition": defs.get(k)
                }
            defs = [toMap(k) for k in defs.keys()]
            memcache.add("def:vocab-list", defs, 86400 * 15)
        
        return webapp2.Response(json.dumps(defs[offset:length]))

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
    