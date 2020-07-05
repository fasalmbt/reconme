import requests as r 
import sys

def zonetransfer(url):
	gotcha = r.get('https://api.hackertarget.com/zonetransfer/?q='+url).text
	sys.stdout.write(gotcha)
	print("\n")