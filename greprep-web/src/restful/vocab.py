
import webapp2, logging
from google.appengine.api import memcache
from words.dictref import *

class VocabListResourceHandler(webapp2.RequestHandler):
    def get(self):
        with open("data/majortests.json") as f:
            self.response.write(f.read())

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
    