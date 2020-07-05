import requests as r 
import sys

def httpheaders(url):
	gotcha = r.get('https://api.hackertarget.com/httpheaders/?q='+url).text
	sys.stdout.write(gotcha)
	print("\n")