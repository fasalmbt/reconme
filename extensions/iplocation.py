import requests as r
import sys

def iplocate(url):
	gotcha = r.get('https://api.hackertarget.com/geoip/?q='+url).text
	sys.stdout.write(gotcha)