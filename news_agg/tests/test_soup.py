from django.test import TestCase
from ..modules.websites.screen_rant import ScreenRant
from ..modules.websites.collider import Collider
from ..modules.websites.ign import Ign
from bs4 import BeautifulSoup
from bs4.element import Tag
from datetime import datetime


class SoupBaseTest():

    def setUp(self):
        req = self.instance.request_website()
        self.soup = self.instance.make_soup(req.text)
        self.articles = self.instance.find_articles(self.soup)


    def test_articles_len(self):
        articles = self.articles

        self.assertTrue(isinstance(articles, list))
        self.assertTrue(isinstance(articles[0], Tag))

    def test_title(self):
        article = self.articles[0]
        title = self.instance.find_title(article)
        print(title)

        self.assertTrue(isinstance(title, str))


    def test_paragraph(self):
        article = self.articles[0]
        paragraph = self.instance.find_paragraph(article)
        print(paragraph)

        self.assertTrue(isinstance(paragraph, str))

    
    def test_image(self):
        article = self.articles[0]
        image = self.instance.find_image(article)
        print(image)

        self.assertTrue(isinstance(image, str))


    def test_link(self):
        article = self.articles[0]
        link = self.instance.find_link(article)
        print(link)

        self.assertTrue(isinstance(link, str))


    def test_date(self):
        article = self.articles[3]
        date = self.instance.find_date(article)
        print(date)

        self.assertTrue(isinstance(date, datetime))

    def test_date(self):
        article = self.articles[3]
        date = self.instance.find_date(article)
        print(date)

        self.assertTrue(isinstance(date, datetime))

    
    def test_logo(self):
        logo = self.instance.find_logo(self.soup)
        print(logo)

        self.assertTrue(isinstance(logo, dict))
        self.assertTrue(isinstance(logo['val'], str))



class ScreenRantClassTestCase(SoupBaseTest, TestCase):
    def setUp(self):
        self.instance = ScreenRant()
        super().setUp()

class ColliderClassTestCase(SoupBaseTest, TestCase):
    def setUp(self):
        self.instance = Collider()
        super().setUp()

class IgnClassTestCase(SoupBaseTest, TestCase):
    def setUp(self):
        self.instance = Ign()
        super().setUp()