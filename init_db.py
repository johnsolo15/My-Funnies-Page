from funnies_page import app, mongo
from comic_scraper import scrape_gocomics, scrape_comicskingdom

def main():
    with app.app_context():
        comics = scrape_gocomics() + scrape_comicskingdom()
        mongo.db.comics.drop()
        mongo.db.comics.insert_many(comics)
        print('Database populated')

if __name__ == '__main__':
    main()
