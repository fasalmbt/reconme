import requests as r
import sys

def nslookup(url):
	gotcha = r.get('http://api.hackertarget.com/dnslookup/?q='+url).text
	sys.stdout.write(gotcha)
	print("\n")