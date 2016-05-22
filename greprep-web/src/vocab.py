
import webapp2
import words.dictref

class VocabResourceHandler(webapp2.RequestHandler):
    def get(self):
        with open("data/majortests.json") as f:
            self.response.write(f.read())

    