#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Creates a web page to encrypt plaintext using the Caesar cypher
"""
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
from cgi import escape
import caesar


def build_page(stuff=""):
    """builds the page
    """
    # <!-- Latest compiled and minified CSS -->
    header = """<link rel="stylesheet"
    href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"
    integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u"
    crossorigin="anonymous">
    """

# <!-- Optional theme -->
    header += """ <link rel="stylesheet"
    href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css"
    integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp"
    crossorigin="anonymous">
    """

# <!-- Latest compiled and minified JavaScript -->
    header += """ <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"
    integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa"
    crossorigin="anonymous"></script>
    """

    header += '<link type="text/css" rel="stylesheet" href="/static/css/normalize.css">'
    header += '<link type="text/css" rel="stylesheet" href="/static/css/caesar.css">'
    header += '<h1>Enter a message for Caesar.</h1><div class="container">'

    a_form = """<form method="POST"><label for="rot">Rotate by:
        <input name="rot" type="number" id="rot" class="rot"></label>
            <label for="ta">Enter text below:
                <textarea name="message" id="ta" class="ta">"""
    a_form += stuff
    a_form += """</textarea></label><input type="submit" class="submit"
    value="Encrypt"></input></form></div>"""
    content = header + a_form
    return content



class MainHandler(webapp2.RequestHandler):
    """ Gets here via /
    """
    def get(self):
        """ inits page
        """
        self.response.write(build_page())


    def post(self):
        """ encrypts message
        """
        plain_text = self.request.get('message')
        rot = self.request.get('rot')
        try:
            rot = int(rot)
            encrypted_text = caesar.encrypt(plain_text, rot)
        except ValueError:
            encrypted_text = 'Invalid rotation amount. ' + rot
        self.response.write(build_page(escape(encrypted_text)))


app = webapp2.WSGIApplication([
    ('/', MainHandler)
    ], debug=True)
