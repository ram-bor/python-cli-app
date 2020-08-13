from model import Bookmark

# Greet User
print(f'\nWelcome to Bookmark Collector! Here, you can add personal bookmarks.\nAdd as many as you\'d like! :)\n')

def new_bookmark():
    user_answer = input(f'Would you like to create a new bookmark? (y/n) ')
    if user_answer == 'y':
        add_bookmark()
    if user_answer == 'n':
        exit()

def add_bookmark():
    temp_title = add_title()
    temp_link = add_link()
    temp_details = add_details()
    bm = Bookmark(title=temp_title, link=temp_link, details=temp_details)
    bm.save()

def add_title():
    bookmark_title = input(f'Please enter a webpage title: ')   
    return bookmark_title
    bookmark_title.save()
pass

def add_link():
    bookmark_link = input(f'Please add webpage url: ')
    return bookmark_link
    bookmark_link.save()
pass    

def add_details():
    bookmark_details = input(f'Please add any webpage details: ')    
    return bookmark_details
    bookmark_details.save()
pass


new_bookmark()


# class BookmarkApp:
#     def __init__(self, title, link, details):
#         self.title = []
#         self.link = []
#         self.details = []

#     def append(self, title, link, details):
#         if isinstance(temp_title, title):
#             self.title.append(title)
#         if isinstance(temp.link, link):
#             self.link.append(link)
#         if isinstance(temp_details, details):
#             self.details.append(details)
# pass

# new_bookmark = BookmarkApp()
# print(new_bookmark)