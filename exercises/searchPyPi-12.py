#!/usr/bin/python3

import requests, sys, bs4, webbrowser

print('Searching...') #display text while searching

res = requests.get('https://pypi.org/search/?q=' + '+'.join(sys.argv[1:]))

res.raise_for_status()

#retrieve top search links
soup = bs4.BeautifulSoup(res.text, 'html.parser')

#open a browser tab for each result
linkElems = soup.select('.package-snippet')
numOpen = min(5, len(linkElems))

for i in range(numOpen):
	urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
	print('Opening', urlToOpen)
	webbrowser.open(urlToOpen)
