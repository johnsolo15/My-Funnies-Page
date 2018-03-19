from funnies_page import db
from funnies_page.models import Comic
from comic_scraper import scrape_gocomics, scrape_comicskingdom

def load_db():
    comics = scrape_gocomics() + scrape_comicskingdom()
    for c in comics:
        comic = Comic(name=c['name'], source=c['src'])
        db.session.add(comic)
    db.session.commit()
    print('Database populated')

if __name__ == '__main__':
    load_db()
