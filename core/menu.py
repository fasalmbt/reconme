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
from extensions.subnetlookup import subnetlookup
from extensions.wayback import wayback


def continue_else():
	con = input("Sorry ! That was a wrong choice. Do you want to continue(Y/N) ")
	if con == 'Y' or con == 'y':
		menu()
	else:
		print("Bye!")
		exit()

def continue_choice():
	con = input("Do you want to continue(Y/N) ")
	if con == 'Y' or con == 'y':
		menu()
	else:
		print("Bye!")
		exit()

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
	print("11 - Subnet Lookup")
	print("12 - Wayback URL's")
	choice = int(input("\nEnter your choice >> "))
	if choice == 1:
		whois(url)
		continue_choice()
	elif choice == 2:
		url = args.u
		nslookup(url)
		continue_choice()
	elif choice == 3:
		url = str(input("Enter the domain/IP >> "))
		robots(url)
		continue_choice()
	elif choice == 4:
		url = str(input("Enter the domain >> "))
		admin(url)
		continue_choice()
	elif choice == 5:
		url = str(input("Enter the IP >> "))
		iplocate(url)
		continue_choice()
	elif choice == 6:
		url = str(input("Enter the domain/IP >> "))
		portscan(url)
		continue_choice()
	elif choice == 7:
		url = str(input("Enter the IP >> "))
		reverseip(url)
		continue_choice()
	elif choice == 8:
		url = str(input("Enter the domain/IP >> "))
		forwardns(url)
		continue_choice()
	elif choice == 9:
		url = str(input("Enter the domain/IP >> "))
		httpheaders(url)
		continue_choice()
	elif choice == 10:
		url = str(input("Enter the domain/IP >> "))
		zonetransfer(url)
		continue_choice()
	elif choice == 11:
		url = str(input("Enter the domain/IP >> "))
		subnetlookup(url)
		continue_choice()
	elif choice == 12:
		url = str(input("Enter the domain/IP >> "))
		wayback(url)
		continue_choice()
	else:
		continue_else()

