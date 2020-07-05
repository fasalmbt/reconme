import requests as r
import sys

def whois(url):
	gotcha = r.get('https://api.hackertarget.com/whois/?q='+url).text
	print("\n")
	sys.stdout.write(gotcha)