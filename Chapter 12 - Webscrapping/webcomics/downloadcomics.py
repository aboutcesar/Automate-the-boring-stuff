import os, requests
import bs4

# load homepage
url = 'https://xkcd.com/'


#Retrive
os.makedirs('xkcd', exist_ok = True)



while not url.endswith('#'):
    #downloads the page
    print('Downloading...')
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')


    # find the comic url
    comicElems = soup.select('#comic img')
    if comicElems == []:
        print('picture')
    else:
        comicUrl = 'https:' + comicElems[0].get('src')
        #download the image
        res = requests.get(comicUrl)
        res.raise_for_status()

        #Save to xcdk
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')
    
        
    

        
        
        
        
        
    
      
