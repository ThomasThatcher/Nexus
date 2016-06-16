import os
import sys
import cpanel
from lxml import html
from lxml.cssselect import CSSSelector

class Server:

	class Apache:

		def __init__(self):
			pass

		def avaliable_apache_modules(self):
			return cPanel.shell("httpd -l")

		def httpd_version(self):
			return cPanel.shell("httpd -v")

		def lsws_installed(self):
			return os.path.exists("/usr/local/lsws")

		def lsws_version(self):
			return open("/usr/local/lsws/VERSION").read()

		def check_lsws_latest_version(self):
			page = requests.get('litespeedtech.com/products/litespeed-web-server/release-log')
			tree = html.fromstring(page.content)
			version = tree.cssselect('tbody tr:first-child strong')
			return version

	class Exim:

		def __init__(self):
			self.version = cPanel.shell("exim --version")
			self.queue = cPanel.shell("exim -bpc")

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
			self.php_versions = cPanel.shell("selectorctl --summary --show-native-version")

		def avaliable_php_modules(self):
			return cPanel.shell("php -m")

		def get_user_php_version(self, user):
			return cPanel.shell("selectorctl --summary --current --user=" + user)

		def get_user_python_version(self, username):
			return cPanel.shell("selectorctl --interpreter=python --summary --current --user=" + user)

		def get_user_ruby_version(self, username):
			return cPanel.shell("selectorctl --interpreter=ruby --summary --current --user=" + user)