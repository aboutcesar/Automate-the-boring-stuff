import bs4, sys, requests

# load homepage
url = 'https://xkcd.com/'


#Retrive
os.makedirs('xkcd', exist_ok = true)



while not url.endswith('#'):
    #downloads the page
    print('Downloading...')
    res = request.get(url)
    res.status_code()
    soup = bs4.beautifulsoup4(res.text, 'html.parser')


    # find the comic url
    comicElem = soup.selec('#comic img')
    if comicElem = []:
        print('picture')
    else:
        comicUrl = 'https://' + comicElems.get('src')
        #download the image
        res = request.get(comicUrl)
        res.raise_for_status()

        #Save to xcdk
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')
    
        
    

        
        
        
        
        
    
      
