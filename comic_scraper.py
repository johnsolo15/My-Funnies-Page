import requests
import time
from bs4 import BeautifulSoup

GOCOMICS_BASE_URL = 'http://www.gocomics.com'
GOCOMICS_LIST_URL = 'http://www.gocomics.com/comics/a-to-z'
COMICSKINGDOM_BASE_URL = 'http://comicskingdom.com'
COMICSKINGDOM_LIST_URL = 'http://comicskingdom.com/comics'

def scrape_gocomics():
    res = requests.get(GOCOMICS_LIST_URL)
    res.raise_for_status()
    html = BeautifulSoup(res.text, 'html.parser')
    comic_names = html.select('a h4.media-heading')
    comic_names = [x.getText() for x in comic_names]
    comic_pages = html.select('.amu-media-item-link')
    comic_pages = [GOCOMICS_BASE_URL + x.get('href')
                   for x in comic_pages]
    comic_imgs = []
    for url in comic_pages:
        try:
            res = requests.get(url)
            res.raise_for_status()
        except Exception as err:
            print(err)
            continue
        html = BeautifulSoup(res.text, 'html.parser')
        src = html.select('.item-comic-image img')[0].get('src')
        comic_imgs.append(src)
        time.sleep(1)
    comics = []
    for name, url in zip(comic_names, comic_imgs):
        comics.append({'name': name, 'src': url})
    return comics

def scrape_comicskingdom():
    res = requests.get(COMICSKINGDOM_LIST_URL)
    res.raise_for_status()
    html = BeautifulSoup(res.text, 'html.parser')
    comic_links = html.select('.on div.col a')
    comics = []
    for link in comic_links:
        try:
            res = requests.get(link.get('href'))
            res.raise_for_status()
        except Exception as err:
            print(err)
            continue
        html = BeautifulSoup(res.text, 'html.parser')
        if html.select('.feature-blog-post h4 a'):
            try:
                res = requests.get(html.select('.feature-blog-post h4 a')[0].get('href'))
                res.raise_for_status()
            except Exception as err:
                print(err)
                continue
            html = BeautifulSoup(res.text, 'html.parser')
            src = html.select('form img')[0].get('src')
            comics.append({'name': link.getText(), 'src': src})
        time.sleep(1)
    return comics
