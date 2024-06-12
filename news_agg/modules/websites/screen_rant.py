from ..base.soup_base import soup_base 
from datetime import datetime, timezone



class ScreenRant(soup_base):

    def __init__(self):
        self.name = 'Screen Rant'
        self.url = 'https://screenrant.com/'
        super().__init__()


    def find_articles(self, soup):
        sp = soup.find(class_="sentinel-home-list")
        sp = sp.find_all(class_='article')
        return sp

    def find_title(self, article):
        title = article.h5.a.text
        return title

    def find_paragraph(self, article):
        paragraph = article.p.text
        return paragraph

    def find_image(self, article):
        img = article.find('div', class_="img-displayCard").img['src']
        return img

    def find_link(self, article):
        link = article.h5.a['href']
        link = self.url + link
        return link

    def find_date(self, article):
        get_date = article.time['datetime']
        date_format = '%Y-%m-%dT%H:%M:%SZ'
        date = datetime.strptime(get_date, date_format).replace(tzinfo=timezone.utc)

        return date

    def find_logo(self, soup):
        logo = 'https://screenrant.com/public/build/images/sr-logo-full-colored-light.svg'
        return {'type':'link', 'val': logo}