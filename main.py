#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2007 Google Inc.
# copyright © Philip R. Huffman 2017 all rights reserved.
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
import webapp2
import caesar
from cgi import escape


def buildPage(stuff=""):
    # <!-- Latest compiled and minified CSS -->
    header = '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">'

# <!-- Optional theme -->
    header += '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">'

# <!-- Latest compiled and minified JavaScript -->
    header += '<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>'
    header += '<link type="text/css" rel="stylesheet" href="/static/css/normalize.css">'
    header += '<link type="text/css" rel="stylesheet" href="/static/css/caesar.css">'
    header += '<h1>Enter a message for Caesar.</h1><div class="container">'
    aForm = '<form method="POST"><label for="rot">Rotate by:' + \
            '<input name="rot" type="number" id="rot" class="rot"></label>'+ \
            '<label for="ta">Enter text below:' + \
            '<textarea name="message" id="ta" class="ta">' + stuff +\
            '</textarea></label><input type="submit" class="submit" value="Encrypt"></input></form></div>'
    content = header + aForm
    return content



class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(buildPage())


    def post(self):
        plainText = self.request.get('message')
        rot = self.request.get('rot')
        try:
            rot = int(rot)
            encryptedText = caesar.encrypt(plainText, rot)
        except ValueError:
            encryptedText = 'Invalid rotation amount. ' + rot
        self.response.write(buildPage(escape(encryptedText)))


app = webapp2.WSGIApplication([
    ('/', MainHandler)
    ], debug=True)
