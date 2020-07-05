import requests as r
import sys

def portscan(url):
	gotcha = r.get('https://api.hackertarget.com/nmap/?q='+url).text
	print("\n")
	sys.stdout.write(gotcha)