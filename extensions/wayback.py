import requests as r
import sys
import os

def wayback(url):
	gotcha = r.get("https://web.archive.org/cdx/search/cdx?url=%s/*&output=text&fl=original&collapse=urlkey"%url).text
	ch_wayback = str(input("Hey , file may be too large. Wanna save in a txt file (Y/N)? "))
	if ch_wayback == "y" or ch_wayback == "Y":
		filename = "site_wayback.txt"
		file = open(filename, "w")
		file.write(gotcha)
		file.close()
		print("Saved to "+filename)
		qu = str(input("You wanna filter endpoints and save it in a txt file (Y/N)? "))
		if qu == "Y" or qu == "y":
			os.system("cat site_wayback.txt | grep '=' > endpoints.txt")
			print("Saved to endpoints.txt")
	else:
		sys.stdout.write(gotcha)