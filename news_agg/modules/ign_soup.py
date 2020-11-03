from .base.soup_base import soup_base 




class ign_soup(soup_base):

    def get_base_url(self):
        return 'https://br.ign.com/'

    def find_website_logo(self, soup):
        logo = soup.select("#headerlogo .ign-logo")[0]
        return logo

    def find_articles(self, soup):
        articles = soup.find_all("article", class_="article NEWS")
        return articles

    def website_name(self):
        return 'IGN'

    def find_title(self, article):
        title = article.find('h3').get_text()
        return title


    def find_paragraph(self, article):
        paragraph = article.find('p').get_text()
        return paragraph

    def find_image(self, article):
        image = article.find('img', class_="thumb").get('src')
        return image

    def find_link(self, article):
        link = article.find(['h3', 'a']).get('href')
        return link

    def find_date(self, article):
        find_date = article.find('time').get('datetime')

        input_date_format = '%Y-%m-%dT%H:%M:%S%z'

        defined_date = self.define_dates(find_date, input_date_format)
        

        return defined_date
