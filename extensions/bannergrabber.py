import requests as r
import sys 

def ban_grab(url):
    gotcha = r.get('https://api.hackertarget.com/bannerlookup/?q='+url).text 
    sys.stdout.write(gotcha)
    print("\n")