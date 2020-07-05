#menu.py
from extensions.whois import whois
from extensions.admin import admin
from extensions.iplocation import iplocate
from extensions.nslookup import nslookup
from extensions.robots import robots
from extensions.portscan import portscan
from extensions.reverseip import reverseip

def menu():
	print("1 - Whois Lookup\n")
	print("2 - NameServer Lookup\n")
	print("3 - Robots.txt Scanner\n")
	print("4 - Admin Panel Scanner\n")
	print("5 - Find IP address location\n")
	print("6 - TCP Port Scan\n")
	print("7 - Reverse IP Lookup\n")
	choice = int(input("Enter your choice:-"))
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
	else:
		print("Sorry bro! That was a wrong choice.")
		exit()

