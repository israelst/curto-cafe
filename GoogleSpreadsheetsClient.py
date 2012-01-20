#!/usr/bin/python

import re, urllib, urllib2

class GoogleSpreadsheetsClient(object):
	def __init__(self, email, password):
		super(GoogleSpreadsheetsClient, self).__init__()
		self.email = email
		self.password = password
	
	def _get_auth_token(self, email, password, source, service):
		url = "https://www.google.com/accounts/ClientLogin"
		params = {
			"Email": email, "Passwd": password,
			"service": service,
			"accountType": "HOSTED_OR_GOOGLE",
			"source": source
		}
		req = urllib2.Request(url, urllib.urlencode(params))
		return re.findall(r"Auth=(.*)", urllib2.urlopen(req).read())[0]

	def get_auth_token(self):
		source = type(self).__name__
		return self._get_auth_token(self.email, self.password, source, service="wise")
			
	def get_spreadsheet(self, spreadsheet_id, gid=0, export_format="csv"):
		url_format = "https://spreadsheets.google.com/feeds/download/spreadsheets/Export?key=%s&exportFormat=%s&gid=%i"
		headers = {
			"Authorization": "GoogleLogin auth=" + self.get_auth_token(),
			"GData-Version": "3.0"
		}
		req = urllib2.Request(url_format % (spreadsheet_id, export_format, gid), headers=headers)
		return urllib2.urlopen(req)

if __name__ == "__main__":
	import getpass
	import csv
	
	email = "" # (your email here)
	password = getpass.getpass()
	spreadsheet_id = "" # (spreadsheet id here)

	# Create a client object
	gs = GoogleSpreadsheetsClient(email, password)
	
	# Request a file-like object containing the spreadsheet's contents
	csv_file = gs.get_spreadsheet(spreadsheet_id)
	
	# Parse as CSV and print the rows
	for row in csv.reader(csv_file):
		print ", ".join(row)
