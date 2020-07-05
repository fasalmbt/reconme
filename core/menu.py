from extensions.whois import whois
from extensions.admin import admin
from extensions.iplocation import iplocate
from extensions.nslookup import nslookup
from extensions.robots import robots
from extensions.portscan import portscan
from extensions.reverseip import reverseip
from extensions.forwardns import forwardns
from extensions.httpheaders import httpheaders
from extensions.zonetransfer import zonetransfer

def menu():
	print("1  - Whois Lookup")
	print("2  - NameServer Lookup")
	print("3  - Robots.txt Scanner")
	print("4  - Admin Panel Scanner")
	print("5  - Find IP address location")
	print("6  - TCP Port Scan")
	print("7  - Reverse IP Lookup")
	print("8  - Forward DNS search")
	print("9  - HTTP Headers Check")
	print("10 - Zone Transfer")
	choice = int(input("\nEnter your choice:-"))
	url = str(input("Enter the URL:-"))
	if choice == 1:
		whois(url)
	elif choice == 2:
		nslookup(url)
	elif choice == 3:
		robots(url)
	elif choice == 4:
		admin(url)
	elif choice == 5:
		iplocate(url)
	elif choice == 6:
		portscan(url)
	elif choice == 7:
		reverseip(url)
	elif choice == 8:
		forwardns(url)
	elif choice == 9:
		httpheaders(url)
	elif choice == 10:
		zonetransfer(url)
	else:
		print("Sorry bro! That was a wrong choice.")
		exit()

