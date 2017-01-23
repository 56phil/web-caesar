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
import helpers

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = '<link type="text/css" rel="stylesheet" href="/static/css/normalize.css">'
        header += '<link type="text/css" rel="stylesheet" href="/static/css/caesar.css">'
        header += '<div class="container"><h1>Enter text for Caesar:</h1>'
        aForm = '<form><textarea class="ta"></textarea><input type="submit" class="submit"></form>'
        content = header
        content += aForm + '</div>'
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
