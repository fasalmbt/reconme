import urllib.request as r
import urllib.error as e
import os
import sys
def admin(url):
	with open(os.path.join(sys.path[0], "extensions/admin.txt")) as link:
		links = link.readlines()
		for admin_link in links:
			request = "https://"+url+"/"+admin_link
			try:
				req = r.urlopen(request)
				code = req.getcode()
				if code == 200:
					print("admin panel ==> "+request)
					break
			except e.URLError as err:
				print("Sorry not found at ==> "+request)