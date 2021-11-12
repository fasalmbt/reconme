import requests as r 
import sys

def reverseip(url):
	gotcha = r.get('https://api.hackertarget.com/reverseiplookup/?q='+url).text
	print("\n")
	sys.stdout.write(gotcha)
	print()