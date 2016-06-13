import os
import sys

class cPanel:

	# Run a shell command and return the results.
	def shell(command):
		return os.system(command)

	# Find all DNS records for a given domain name, and output them into a dictionary.
	# E.g. Something that looks a little like this.
	#	{
	#		"a"    :"x.x.x.x",
	#		"aaaa" :"x.x.x.x",
	#		"mx"   :"host.domain.com",
	#		"cname":"host.domain.com",
	#		"txt"  :"v=spf1 a:mail.domain.com ~all"
	#	}
	def domain_records(domain):
		records = ["a","aaaa","mx","cname","txt"]
		return dict(zip(records, [(lambda r: cPanel.shell("dig " + r + domain + " +short"))(records)]))

	class Server:

		class Apache:

			def __init__(self):
				pass

		class Exim:

			def __init__(self):
				pass

		class Firewall:

			def __init__(self):
				pass

		class DNS:

			def __init__(self):
				pass

		class WAF:

			def __init__(self):
				pass

		class CXS:

			def __init__(self):
				self.version = cPanel.shell("cxs --version")
				self.location = "/home/quarantine/cxsuser/"
				self.users = self.quarantined_users()

			def scan_user(self, username):
				return cPanel.shell("cxs --user" + username)

			def quarantined_users(self):
				return os.listdir(self.location)

			def users_quarantined_files(self, username):
				return os.listdir(self.location + username)

		class CloudLinux:

			def __init__(self):
				pass

	# The Following code genrates something that looks like this.
	# 	---> self.dns = dict(zip(self.domains), [(lambda x: cPanel.domain_records(x))(self.domains)])
	#
	#	{
	#		"example.com": 
	#		{
	#			"a"    :"x.x.x.x",
	#			"aaaa" :"x.x.x.x",
	#			"mx"   :"host.domain.com",
	#			"cname":"host.domain.com",
	#			"txt"  :"v=spf1 a:mail.domain.com ~all"
	#		},
	#
	#		"example.com": 
	#		{
	#			"a"    :"x.x.x.x",
	#			"aaaa" :"x.x.x.x",
	#			"mx"   :"host.domain.com",
	#			"cname":"host.domain.com",
	#			"txt"  :"v=spf1 a:mail.domain.com ~all"
	#		}
	#	}
	#
	#

	class User:

		def __init__(self, domain_name):
			self.domain_name = domain_name
			self.username = cPanel.shell("/scripts/whoowns " + self.domain_name)
			self.domains = os.listdir('/var/cpanel/userdata/' + self.username)
			self.dns = dict(zip(self.domains), [(lambda x: cPanel.domain_records(x))(self.domains)])

	class CMS:

		def __init__(self):

		class WordPress:

			def __init__(self):
				pass

			def find_wordpress(self, directory, depth):
				for f in os.listdir(directory):
					

		class Joomla:

			def __init__(self):
				pass

		class Drupal:

			def __init__(self):
				pass

		class Megento:

			def __init__(self):
				pass

		class Prestashop:

			def __init__(self):
				pass

		class PHPBB:

			def __init__(self):
				pass