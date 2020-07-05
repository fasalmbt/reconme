import requests as r

def robots(url):
	robot = 'https://'+url+'/robots.txt'
	reqq = r.get(robot)
	if '<html>' not in reqq.text:
		print("Found robots.txt ==> "+robot)
	else:
		print("Sorry! robots.txt not found")