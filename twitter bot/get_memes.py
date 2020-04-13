import requests 
from bs4 import BeautifulSoup as bs
import os

url = ""

page = requests.get(url)
soup = bs(page.text, "html.parser")

image_tags = soup.findAll('img')

if not os.path.exists('models'):
    os.makedirs('models')

os.chdir('models')

x=0

for image in image_tags:
    try:
        ulr = image['src']
        source = requests.get(url)
        if source.status_code == 200:
            with open('model-' + str(x) + '.jpg', 'wb') as f:
                f.write(requests(url).content)
                f.close()
                x+=1
    except:
        pass