from .base.soup_base import soup_base 



class theenemy_soup(soup_base):

    def get_base_url(self):
        return 'https://www.theenemy.com.br/'

    def find_website_logo(self, soup):
        logo = soup.select(".header__top__brand")[0] 
        return logo
    
    def find_articles(self, soup):
        articles = soup.select('.news-list--big div.news-list__item')
        return articles

    def website_name(self):
        return 'The Enemy'

    def find_title(self, article):
        title = article.select('.news-list__item__content__title')[0].get_text()
        return title

    def find_paragraph(self, article):
        paragraph = article.p.get_text()
        return paragraph

    def find_image(self, article):
        image = article.img.get('src')
        return image

    def find_link(self, article):
        link = article.a.get('href')
        replaced_link = link.replace('/', self.get_base_url(), 1)
        return replaced_link

    def find_date(self, article):
        find_date = article.select('.news-list__item__content__info__time')[0].get_text()

        input_date_format = '%d.%m.%Y %HH%M' 

        defined_date = self.define_dates(find_date, input_date_format)
        

        return defined_date