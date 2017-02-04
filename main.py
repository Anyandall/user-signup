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
import string


form = """
<h2>Signup</h2>
<form method='post'>
	<label>Username</label>
	<input type='text' name='UserName'/><br>
	<label>Password</label>
	<input type='password' name='Password'/><br>
	<label>Verify Password</label>
	<input type='password' name='VerifyPassword'/><br>
	<label>Email (optional)</label>
	<input type='email' name='Email'/><br>
	<br>
	<input type='submit'/>
</form>
"""

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
	
	return form
	
def valid_username(username):
	invalid_characters = string.punctuation
	for character in username:
	    if character in invalid_characters:
	        print (username + " contains the following invalid character: " + character)
	        return False
	print (username + " is a valid username!")
	return True

class MainHandler(webapp2.RequestHandler):
	def get(self):
		content = build_page("")
		self.response.write(content)
		
	def post(self):
		username = self.request.get("UserName")
		greeting = "Thanks for logging in, " + username + "!"
		if not valid_username(username):
			self.response.write(form)
		else:
			self.response.write(greeting)
		
class WelcomeHandler(webapp2.RequestHandler):
	def get(self):
		self.response.write("Welcome, ")
		

app = webapp2.WSGIApplication([
    ('/', MainHandler),
	('/Welcome', WelcomeHandler)
], debug=True)
