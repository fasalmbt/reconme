import requests as r
import sys

def whois(url):
	gotcha = r.get('http://api.hackertarget.com/whois/?q='+url).text
	sys.stdout.write(gotcha)