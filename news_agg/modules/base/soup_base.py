from bs4 import BeautifulSoup as BSoup
from datetime import datetime
import requests






# base
class soup_base:
    def __init__(self):
        self.website_components_list = self.get_website_data()

    def get_website_data(self):

        try:
            website_request = requests.get(self.get_base_url())
                
        except requests.exceptions.RequestException as error:
            raise error

        
        
        soup = self.make_soup(website_request.text)


        articles_finded = self.find_articles(soup)
        articles_list = self.get_articles_list(articles_finded)

        website_logo = self.find_website_logo(soup)

        website_components_list = {'logo': website_logo, 'articles': articles_list}
        return website_components_list


    def make_soup(self, website):
        soup = BSoup(website, 'html.parser')
        return soup

    def define_dates(self, date, input_date_format):
        now_date = datetime.now(tz=None)

        posted_date = datetime.strptime(date, input_date_format).replace(tzinfo=None)

        time_since_posted_subtraction = now_date - posted_date
        seconds = time_since_posted_subtraction.total_seconds()

        days, seconds = divmod(seconds, 86400)
        hours, seconds = divmod(seconds, 3600)
        minutes, seconds = divmod(seconds, 60)

        time_since_posted = 'há '


        if days > 0:
            time_since_posted += f'{int(days)} dias, '

        if hours > 0:
            time_since_posted += f'{int(hours)} horas, '

        if minutes > 0:
            time_since_posted += f'{int(minutes)} minutos'


        output_date_format = '%Y-%m-%dT%H:%M:%S'
        output_posted_date = posted_date.strftime(output_date_format)

        result = {
            'posted_date': output_posted_date,
            'time_since_posted': time_since_posted
        }

        return result



    def get_articles_list(self, articles):

        title_list = [self.find_title(article) for article in articles]

        paragraph_list = [self.find_paragraph(article)
            for article in articles]

        image_list = [self.find_image(article) for article in articles]

        link_list = [self.find_link(article)
            for article in articles]


        date_list = [self.find_date(article)
            for article in articles]



        result_articles_list = [
            {'title': title, 'paragraph': paragraph, 'image': image, 'link': link, 'date': date, 'website_name': self.website_name}
            for title, paragraph, image, link, date
            in zip(title_list, paragraph_list, image_list,
            link_list, date_list)]

        return result_articles_list


    def website_name(self):
        raise NotImplementedError("Must override website_name")

    def find_website_logo(self, soup):
        raise NotImplementedError("Must override find_website_logo")

    def get_base_url(self):
        raise NotImplementedError("Must override get_base_url")

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
