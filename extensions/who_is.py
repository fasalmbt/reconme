from whois import whois

def who_is(url):
	who = whois(url)
	print(who)
	print("\n")