from extensions.who_is import who_is
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
from extensions.bannergrabber import ban_grab


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
	print("6  - Port Scan")
	print("7  - Reverse IP Lookup")
	print("8  - Forward DNS search")
	print("9  - HTTP Headers Check")
	print("10 - Zone Transfer")
	print("11 - Subnet Lookup")
	print("12 - Wayback URL's")
	print("13 - Banner grabber")
	choice = int(input("\nEnter your choice >> "))
	if choice == 1:
		url = input("Enter domain/IP >> ")
		who_is(url)
		continue_choice()
	elif choice == 2:
		url = str(input("Enter domain/IP >> "))
		nslookup(url)
		continue_choice()
	elif choice == 3:
		url = str(input("Enter domain/IP >> "))
		robots(url)
		continue_choice()
	elif choice == 4:
		url = str(input("Enter domain >> "))
		admin(url)
		continue_choice()
	elif choice == 5:
		url = str(input("Enter IP >> "))
		iplocate(url)
		continue_choice()
	elif choice == 6:
		url = str(input("Enter IP >> "))
		portscan(url)
		continue_choice()
	elif choice == 7:
		url = str(input("Enter IP >> "))
		reverseip(url)
		continue_choice()
	elif choice == 8:
		url = str(input("Enter domain/IP >> "))
		forwardns(url)
		continue_choice()
	elif choice == 9:
		url = str(input("Enter domain/IP >> "))
		httpheaders(url)
		continue_choice()
	elif choice == 10:
		url = str(input("Enter domain/IP >> "))
		zonetransfer(url)
		continue_choice()
	elif choice == 11:
		url = str(input("Enter domain/IP >> "))
		subnetlookup(url)
		continue_choice()
	elif choice == 12:
		url = str(input("Enter domain/IP >> "))
		wayback(url)
		continue_choice()
	elif choice == 13:
		url = str(input("Enter IP >> "))
		ban_grab(url)
		continue_choice()
	else:
		continue_else()

