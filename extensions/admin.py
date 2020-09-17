import urllib.request as r
import urllib.error as e
def admin(url):
	#add your own list
	links=('admin/', 'admin.php', 'administrator/', 'login.php', 'login/', 'login.html', 'admin.html', 'admin/admin.php',
'admin_login.php', 'admin/account.php', 'admin/login.php', 'login/login.php', 'login/admin.php')
	for admin_link in links:
		request = "https://"+url+admin_link
		try:
			req = r.urlopen(request)
			code = req.getcode()
			if code == 200:
				print("\n")
				print("admin panel ==> "+request)
				break
		except e.URLError as err:
			print("\n")
			print("Sorry not found at ==> "+request)