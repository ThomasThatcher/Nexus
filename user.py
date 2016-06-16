import os
import sys
import cpanel

class User:

	def __init__(self, domain_name):
		self.domain_name = domain_name
		self.username = cPanel.shell("/scripts/whoowns " + self.domain_name)
		self.domains = os.listdir('/var/cpanel/userdata/' + self.username)
		self.dns = dict(zip(self.domains), [(lambda x: cPanel.domain_records(x))(self.domains)])

	def scan(self, cxs):
		cxs.scan_user(self.username)