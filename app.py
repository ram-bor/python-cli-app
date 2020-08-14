from model import Bookmark
from model import db

mycursor = db.cursor()
# mycursor.execute("SELECT * FROM Bookmark")

# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)


# Greet User
def greet_user():
    print(f'\nWelcome to Bookmark Collector! You can add, search, update & delete personal bookmarks.\nLet\'s get started! \n')

    print(f'What would you like to do? \n')

    print(f'|  1 = Add a Bookmark     |')
    print(f'|  2 = Search a Bookmark  |')
    print(f'|  3 = Update a Bookmark  |')
    print(f'|  4 = Delete a Bookmark  |\n')

    num_select = input(f'Type number selection here: ')
    if num_select == '1':
        new_bookmark()

    elif num_select == '2':
        search_bookmark()

    # # elif num_select == '3':
    # #     # update_bookmark()

    # # elif num_select == '4':
    # #     # delete_bookmark()

    else: 
        print("Selection input not valid.")

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
pass

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

def search_bookmark():
    search_title = input(f'Enter bookmark title: ')
    # if search_title == Bookmark.title:
    mycursor.execute(f"SELECT * FROM Bookmark WHERE title = '{search_title}'",)
    myresult = mycursor.fetchone()
    print(myresult)
    # else:
        # print("whoops error")

# def update_bookmark():
# def delete_bookmark():

greet_user()



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