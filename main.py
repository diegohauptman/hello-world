#!/usr/bin/env python

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('This code is in GitHub mirrorred in CSR')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

