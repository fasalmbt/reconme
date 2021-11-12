import nmap

def portscan(url):
	nm = nmap.PortScanner()
	scann = nm.scan(url, '22-443')
	for url in nm.all_hosts():
		for protocol in nm[url].all_protocols():
			lport = nm[url][protocol].keys()
			for port in lport:
				print(port, nm[url][protocol][port]['state'])
