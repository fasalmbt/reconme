import requests as r 
import sys

def subnetlookup(ipadd):
	gotcha = r.get('https://api.hackertarget.com/subnetcalc/?q='+ipadd).text
	print("\n")
	sys.stdout.write(gotcha)
	print("")