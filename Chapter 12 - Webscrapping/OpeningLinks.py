import sys, requests, time, BeautifulSoup4, webbrowser

#Get keyword from commandline
print("searching")
if len(sys.argv) > 1:
    res = requests.get('https://www.google.com/search?q=' 'https://pypi.org/search/?q=' + ''.join(sys.argv[1:]))
    res.status_code
    
#retrieve seach page results
searchsoup = bs4.beautifulsoup(res.text, 'html.parser')

#Open tabs for results
linkElems = soup.select('.package-snippet') 
numOpen = min(5, len(linkelems))
for i in range(numOpen):
        urltoOpen = 'https://pypu.org' + linkelems[i].get('href')
        print('opening ', urltoOpen)
        webbrowser.open(urltoOpen)


time.sleep(4)

