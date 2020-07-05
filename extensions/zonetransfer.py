import requests as r 
import sys

def zonetransfer(url):
	gotcha = r.get('https://api.hackertarget.com/zonetransfer/?q='+url).text
	print("\n")
	sys.stdout.write(gotcha)