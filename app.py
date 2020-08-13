from model import Bookmark

# Greet User
print(f'\nWelcome to Bookmark Collector! Here, you can add personal bookmarks.\nAdd as many as you\'d like! :)\n')

def new_bookmark():
    user_answer = input(f'Would you like to add a bookmark? (y/n) ')
    if user_answer == 'y':
        BookmarkApp.add_bookmark()

class BookmarkApp:
    def __init__(self, title, link, details):
        self.title = []
        self.link = []
        self.details = []

    def add_bookmark(self):    
        if user_answer == 'y':
            self.add_title()
            self.add_link()
            self.add_details()
        else:
            exit()

    def add_title(self):
        bookmark_title = input(f'Please enter a webpage title: ')
        self.title.append(bookmark_title)
        return self.title

    def add_link(self):
        bookmark_link = input(f'Please add webpage url: ')
        self.link.append(bookmark_link)
        return self.link

    def add_details(self):
        bookmark_details = input(f'Please add any webpage details: ')    
        self.details.append(bookmark_details)
        return self.details

        
new_bookmark = Bookmark()
print(new_bookmark)

print(add_bookmark())
