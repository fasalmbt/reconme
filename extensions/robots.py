import requests as r

def robots(url):
	robot = 'https://'+url+'/robots.txt'
	reqq = r.get(robot)
	if '<html>' not in reqq.text:
		print("\n")
		print("Found robots.txt ==> "+robot)
	else:
		print("\n")
		print("Sorry! robots.txt not found")