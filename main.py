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
import webapp2
import cgi

def build_page(textarea_content):

	username_label = "<label>Username</label>"
	username_input = "<input type='text' name='UserName'/>"
	
	password_label = "<label>Password</label>"
	password_input = "<input type='password' name='Password'/>"
	
	verify_label = "<label>Verify Password</label>"
	verify_input = "<input type='password' name='VerifyPassword'/>"
	
	email_label = "<label>Email (optional)</label>"
	email_input = "<input type='email' name='Email'/>"
	
	submit = "<input type='submit'/>"
	form = ("<form method='post'>" +
		username_label + username_input + "<br>" + password_label + password_input + "<br>" + verify_label + verify_input + "<br>" + email_label + email_input + "<br>" + "<br>" + submit + "</form>")
		
	header = "<h2>Signup</h2>"
	
	return header + form

class MainHandler(webapp2.RequestHandler):
	def get(self):
		content = build_page("")
		self.response.write(content)
		
	def post(self):
		username = self.request.get("UserName")
	#	message = self.request.get('message')
	#	rotation = int(self.request.get("rotation"))
	#	encrypted_message = caesar.encrypt(message, rotation)
	#	escaped_message = cgi.escape(encrypted_message)
	#	content = build_page(escaped_message)
		self.response.write("Thanks for logging in, " + username + "!")
		
class WelcomeHandler(webapp2.RequestHandler):
	def get(self):
		self.response.write("Welcome, ")
		

app = webapp2.WSGIApplication([
    ('/', MainHandler),
	('/Welcome', WelcomeHandler)
], debug=True)
