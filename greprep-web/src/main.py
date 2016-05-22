#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2, logging
import os, sys

def initialize():
    reload(sys)
    sys.setdefaultencoding('utf8')
    
    rootdir = os.path.dirname(os.path.abspath(__file__))
    lib = os.path.join(rootdir, 'lib')
    sys.path.append(lib)

initialize()

# BEGIN
import vocab

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.redirect("/index.html")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/api/vocab', vocab.VocabListResourceHandler),
    webapp2.Route(r'/api/vocab/<word:.*>', handler=vocab.VocabResourceHandler)
], debug=True)
