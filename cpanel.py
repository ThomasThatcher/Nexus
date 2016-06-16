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