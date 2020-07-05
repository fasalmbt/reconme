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
	print("1  - Whois Lookup\n")
	print("2  - NameServer Lookup\n")
	print("3  - Robots.txt Scanner\n")
	print("4  - Admin Panel Scanner\n")
	print("5  - Find IP address location\n")
	print("6  - TCP Port Scan\n")
	print("7  - Reverse IP Lookup\n")
	print("8  - Forward DNS search\n")
	print("9  - HTTP Headers Check\n")
	print("10 - Zone Transfer\n")
	choice = int(input("Enter your choice:-"))
	print("\n")
	if choice == 1:
		url = str(input("Enter the URL:-"))
		whois(url)
	elif choice == 2:
		url = str(input("Enter the URL:-"))
		nslookup(url)
	elif choice == 3:
		url = str(input("Enter the URL:-"))
		robots(url)
	elif choice == 4:
		url = str(input("Enter the URL:-"))
		admin(url)
	elif choice == 5:
		url = str(input("Enter the URL:-"))
		iplocate(url)
	elif choice == 6:
		url = str(input("Enter the URL:-"))
		portscan(url)
	elif choice == 7:
		url = str(input("Enter the URL:-"))
		reverseip(url)
	elif choice == 8:
		url = str(input("Enter the URL:-"))
		forwardns(url)
	elif choice == 9:
		url = str(input("Enter the URL:-"))
		httpheaders(url)
	elif choice == 10:
		url = str(input("Enter the URL:-"))
		zonetransfer(url)
	else:
		print("Sorry bro! That was a wrong choice.")
		exit()

