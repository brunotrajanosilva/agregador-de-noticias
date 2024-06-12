from ..base.soup_base import soup_base 
from datetime import datetime, timedelta, timezone



class Ign(soup_base):

    def __init__(self):
        self.name = 'Ign'
        self.url = 'http://www.ign.com/news?setccpref=US'
        super().__init__()


    def find_articles(self, soup):
        sp = soup.find(class_="main-content")
        sp = sp.find_all('div', class_='content-item')
        return sp

    def find_title(self, article):
        title = article.find(class_="item-title").text
        return title

    def find_paragraph(self, article):
        paragraph = article.find(class_="item-subtitle").text
        paragraph = paragraph.split('- ')[1]

        return paragraph

    def find_image(self, article):
        img = article.find('div', class_="item-thumbnail").img['src']
        full_image = img.split('?')
        return full_image[0]

    def find_link(self, article):
        link = article.find('a', class_="item-body")['href']
        link = self.url + link
        return link

    def find_date(self, article):
        now = datetime.now(timezone.utc)
        paragraph = article.find(class_="item-subtitle").text
        time = paragraph.split(' ')[0]
        time_text = time[-1]
        time_number = time[:-1]

        time_delta = None

        if time_text == 'm':
            time_number = int(time_number)
            time_delta = timedelta(minutes=time_number)

        if time_text == 'h':
            time_number = int(time_number)
            time_delta = timedelta(hours=time_number)

        date = now - time_delta

        return date

    def find_logo(self, soup):
        logo = soup.find('svg', class_='ign-icon')
        logo['style'] = 'color: #bf1313'

        return {'type':'html', 'val': str(logo)}