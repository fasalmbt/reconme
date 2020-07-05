import urllib.request as r
import urllib.error as e
def admin(url):
	#add your own list
	links=('/admin','/administrator','/admincp','/apanel','admin/login.php')
	for admin_link in links:
		request = "https://"+url+admin_link
		try:
			req = r.urlopen(request)
			code = req.getcode()
			if code == 200:
				print("admin panel ==> "+request)
				break
		except e.URLError as err:
			print("Sorry not found at ==> "+request)