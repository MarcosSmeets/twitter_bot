import requests 
from bs4 import BeautifulSoup as bs
import os

url = "https://www.facebook.com/pg/ocfreshstolenmemes1/photos/?ref=page_internal"

page = requests.get(url)
soup = bs(page.text, "html.parser")

image_tags = soup.findAll('img')

if not os.path.exists('memes'):
    os.makedirs('memes')

os.chdir('memes')

x=0

for image in image_tags:
    try:
        ulr = image['src']
        source = requests.get(url)
        if source.status_code == 200:
            with open('memes-' + str(x) + '.png', 'wb') as f:
                f.write(requests(url).content)
                x+=1
                f.close()
                
    except:
        pass