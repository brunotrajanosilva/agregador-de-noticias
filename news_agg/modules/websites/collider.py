from ..base.soup_base import soup_base 
from datetime import datetime, timezone

class Collider(soup_base):

    def __init__(self):
        self.name = 'Collider'
        self.url = 'https://collider.com/'
        super().__init__()


    def find_articles(self, soup):
        sp = soup.find('div', class_="sentinel-home-list")
        sp = sp.find_all(class_='article')
        return sp

    def find_title(self, article):
        title = article.find('h5', class_="display-card-title").a.text
        return title

    def find_paragraph(self, article):
        paragraph = article.p.text
        return paragraph

    def find_image(self, article):
        img = article.find('a', class_="dc-img-link").img['src']
        return img

    def find_link(self, article):
        link = article.find('a', class_="dc-img-link")['href']
        link = self.url + link
        return link

    def find_date(self, article):
        get_date = article.time['datetime']
        date_format = '%Y-%m-%dT%H:%M:%SZ'
        date = datetime.strptime(get_date, date_format).replace(tzinfo=timezone.utc)

        return date

    def find_logo(self, soup):
        logo =  'https://collider.com/public/build/images/cl-logo-full-colored-light.svg?v=2.7'
        return {'type':'link', 'val': logo}