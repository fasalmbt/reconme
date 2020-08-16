import requests as r
import sys

def wayback(url):
	gotcha = r.get("https://web.archive.org/cdx/search/cdx?url="+url+"/*&output=text&fl=original&collapse=urlkey").text
	ch_wayback = str(input("Hey , file may be too large. Wanna save in a txt file (Y/N)? "))
	if ch_wayback == "y" or ch_wayback == "Y":
		filename = "site_wayback.txt"
		file = open(filename, "w")
		file.write(gotcha)
		file.close()
		print("Saved to "+filename)
	else:
		sys.stdout.write(gotcha)