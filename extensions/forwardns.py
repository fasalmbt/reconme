import requests as r 
import sys

def forwardns(url):
	gotcha = r.get('https://api.hackertarget.com/hostsearch/?q='+url).text
	print("\n")
	sys.stdout.write(gotcha)