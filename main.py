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
import re


form = """
<h2>Signup</h2>
<form method='post'>
	<table>
		<tr>
			<td><label>Username</label></td>
			<td><input type='text' name='UserName' value='%(username)s'/>
				<span class="username_error" style="color: red">%(username_error)s</span>
			</td>
		</tr>
		<tr>
			<td><label>Password</label></td>
			<td><input type='password' name='Password'/>
				<span class="password_error" style="color: red">%(password_error)s</span>
			</td>
		</tr>
		<tr>
			<td><label>Verify Password</label></td>
			<td><input type='password' name='VerifyPassword'/>
				<span class="verify_error" style="color: red">%(verify_error)s</span>
			</td>
		</tr>
		<tr>
			<td><label>Email (optional)</label></td>
			<td><input type='email' name='Email' value='%(email)s'/>
				<span class="email_error" style="color: red"></span>
			
		</tr>
	</table>
	
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

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")	
def valid_username(username):
	return username and USER_RE.match(username)
#	invalid_characters = string.punctuation + " "
#
#	if len(username) < 8:
#		print ("Username cannot contain less than 8 characters!")
#		return False
#	for character in username:
#	    if character in invalid_characters:
#	        print (username + " contains the following invalid character: " + character)
#	        return False
#	if len(username) > 40:
#		print ("Username cannot contain more than 40 characters!")
#		return False
#	print (username + " is a valid username!")
#	return True
PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
	return password and PASS_RE.match(password)
#	if len(password) < 6:
#		return False
#	return True
	
def match_password(password, verify_password):
	if password == verify_password:
		return True
	return False
	
EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
def valid_email(email):
	return not email or EMAIL_RE.match(email)
#	if "@gmail" in str(email):
#		return True
#	if len(email) == 0:
#		return True
#	return False

class MainHandler(webapp2.RequestHandler):

	def write_form(self, username="", username_error="", password_error="", verify_error="", email="", email_error=""):
		self.response.write(form % {"username": username,
									"username_error": username_error,
									"password_error": password_error,
									"verify_error": verify_error,
									"email": email,
									"email_error": email_error
									})
	
	def get(self):
		self.write_form()
		
	def post(self):
		username = self.request.get("UserName")
		password = self.request.get("Password")
		verify_password = self.request.get("VerifyPassword")
		email = self.request.get("Email")
		
		
		has_valid_username = valid_username(username)
		has_valid_password = valid_password(password)
		has_match_password = match_password(password, verify_password)
		has_valid_email = valid_email(email)
		
		greeting = "Thanks for logging in, " + username + "!"
		if has_valid_username and has_valid_password and has_match_password:
			self.redirect("/Welcome?username=" + username)
		elif not has_valid_username and has_valid_email:
			self.write_form("", "Username must be between 3 and 20 characters.", "", "", email, "")
		elif has_valid_username and not has_valid_password:
			self.write_form(username, "", "Passwords must be between 3 and 20 characters.", "", email, "")
		elif has_valid_username and has_valid_password and not has_match_password:
			self.write_form(username, "", "", "Password does not match!", email, "")
		elif has_valid_username and not has_valid_password and not has_valid_email:
			self.write_form(username, "", "Invalid password.", "", "", "Not a valid email address.")
		
class WelcomeHandler(webapp2.RequestHandler):
	def get(self):
		
		username = self.request.get("username")
		self.response.write("Welcome, " + username + "!")
		

app = webapp2.WSGIApplication([
    ('/', MainHandler),
	('/Welcome', WelcomeHandler)
], debug=True)
