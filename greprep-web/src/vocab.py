
import webapp2, logging
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
        logging.info("Looking up for word: " + word)
        return webapp2.Response(json.dumps(lookupDictionaryCom(word)))
    