import os
import sys
import cpanel

if __name__ == "__main__":
	print "-----------------------------------------------------\n"
	print "cPanel Server and User Checker - Verion 0.1 (Alpha)\n"
	print "-----------------------------------------------------\n"

	arguments = sys.argv
	domain_name = arguments[0]

	user = cPanel.User(domain_name)
	apache = cPanel.Server.Apache
	exim = cPanel.Server.Exim
	firewall = cPanel.Server.Firewall
	dns = cPanel.Server.DNS
	waf = cPanel.Server.WAF
	cxs = cPanel.Server.CXS
	cloudlinux = cPanel.Server.CloudLinux



