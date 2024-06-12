from bs4 import BeautifulSoup as BSoup
from datetime import datetime, timezone
import requests


# base
class soup_base:
    def __init__(self):
        self.articles = []
        self.logo = None

    def fetch_all_articles(self):
        req = self.request_website()
        soup = self.make_soup(req.text)
        articles_finded = self.find_articles(soup)
        logo = self.find_logo(soup)
        self.logo = logo

        for article in articles_finded:
            mounted_article = self.mount_article(article)
            self.articles.append(mounted_article)


    def request_website(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36", 
            
        }
        
        website_request = requests.get(self.url, headers=headers)
        return website_request
                
    
    def make_soup(self, website):
        soup = BSoup(website, 'html.parser')
        return soup

    

    def mount_article(self, article):

        try:
            title = self.find_title(article)
        except:
            title = ''

        try:
            paragraph = self.find_paragraph(article)
        except:
            paragraph = ''
        
        try:
            image = self.find_image(article)
        except:
            image = ''

        try:
            link = self.find_link(article)
        except:
            link = ''

        try:
            get_date = self.find_date(article)
            date = self.define_date(get_date)
        except:
            date = datetime.now()


        mounted_article = {
            'title': title,
            'paragraph': paragraph,
            'image': image,
            'link': link,
            'date': date,
        }

        return mounted_article


    def define_date(self, date):
        new_format = '%Y-%m-%dT%H:%M:%SZ'

        new_date = date.strftime(new_format)
        return new_date


    def get_info(self):
        info = {
            'name': self.name,
            'url': self.url,
            'logo': self.logo,
            'articles': self.articles,
        }

        return info


    def find_articles(self, soup):
        raise NotImplementedError("Must override find_articles")

    def find_title(self, article):
        raise NotImplementedError("Must override find_title")

    def find_paragraph(self, article):
        raise NotImplementedError("Must override find_paragraph")

    def find_image(self, article):
        raise NotImplementedError("Must override find_image")

    def find_link(self, article):
        raise NotImplementedError("Must override find_link")

    def find_date(self, article):
        raise NotImplementedError("Must override find_date")

    def find_logo(self, soup):
        raise NotImplementedError("Must override find_date")
