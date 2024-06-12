
class WebsiteManager:

    def __init__(self):
        self.websites = []

    def add_website(self, website):
        self.websites.append(website)

    def fetch(self):
        for website in self.websites:
            try:
                website.fetch_all_articles()

            except Exception as ex:
                self.websites.remove(website)
                print(f'error: {ex}. Website:{website.name} was removed')

    def get_data(self):
        websites_list = []

        for website in self.websites:
            websites_list.append(website.get_info())

        return websites_list



