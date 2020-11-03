
class create_and_sort_website_data:

    def __init__(self):
        self.websites = []

    def add_website(self, website):
        self.websites.append(website)

    def sort_data(self):
        list_of_all_website_logo = {}
        list_of_all_website_articles = []

        for website in self.websites:
            get_website_articles = website.website_components_list['articles']
            list_of_all_website_articles += get_website_articles

            get_website_logo = website.website_components_list['logo']
            list_of_all_website_logo[website.website_name()] = get_website_logo
        
        list_of_all_website_articles.sort(key=lambda article: article['date']['posted_date'], reverse=True)

        result = {'logo_list': list_of_all_website_logo, 'article_list': list_of_all_website_articles}

        return result
