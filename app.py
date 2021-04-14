from model import Bookmark
from model import db
import re
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
    print(f'|  4 = Delete a Bookmark  |')
    print(f'|  5 = Displays all Bookmarks  |\n')

    num_select = input(f'Type number selection here: ')
    if num_select == '1':
        new_bookmark()

    elif num_select == '2':
        search_bookmark()

    elif num_select == '3':
        update_bookmark()

    elif num_select == '4':
        delete_bookmark()
    
    elif num_select == '5':
        display_all()

    else: 
        print("Selection input not valid.")

def new_bookmark():
    user_answer = input(f'Would you like to create a new bookmark? (y/n) ')
    if user_answer == 'y':
        add_bookmark()
    if user_answer == 'n':
        print("Exiting...")
        exit()

def add_bookmark():
    temp_title = add_title()
    temp_link = add_link()
    temp_details = add_details()
    bm = Bookmark(title=temp_title, link=temp_link, details=temp_details)
    bm.save()
    print('Your bookmark was added!')
pass

def add_title():
    bookmark_title = input(f'Please enter a webpage title: ')   
    return bookmark_title
    # bookmark_title.save()
pass

def add_link():
    bookmark_link = input(f'Please add webpage url: ')
    return bookmark_link
    # bookmark_link.save()
pass    

def add_details():
    bookmark_details = input(f'Please add any webpage details: ')    
    return bookmark_details
    # bookmark_details.save()
pass

def search_bookmark():
    search_title = input(f'Enter bookmark title: ')
    if search_title.lower():
        mycursor.execute(f"SELECT * FROM Bookmark WHERE lower(title) = '{search_title}'")
        myresult = mycursor.fetchone()
        print(myresult)

    elif search_title.upper():
        mycursor.execute(f"SELECT * FROM Bookmark WHERE upper(title) = '{search_title}'")
        myresult = mycursor.fetchone()
        print(myresult)
    else:
        print("Error. Invalid input.")

def update_bookmark():
    print('\n Update options are listed below: \n')
    print(' a = Update Title')
    print(' b = Update URL')
    print(' c = Update Details\n')
    field_update = input(f'Select the letter of the field you would like to update: ')

    if field_update == 'a':
        print('You have selected to update a bookmark title!')
        selected_title = input(f'Enter the TITLE of the bookmark you want to update: ')
        mycursor.execute(f"SELECT * FROM Bookmark WHERE lower(title) = '{selected_title}'")
        title_change = input(f'Enter your title changes here: ')
        mycursor.execute(f"UPDATE Bookmark SET title = '{title_change}' WHERE title = '{selected_title}'")
        db.commit()
        mycursor.execute(f"SELECT * FROM Bookmark WHERE title = '{title_change}'")
        updatedrecord = mycursor.fetchone()
        print(updatedrecord)
    elif field_update == 'b':
        print('You have selected to update a bookmark link!')
        selected_link = input(f'Enter the TITLE of the bookmark link you want to update: ')
        mycursor.execute(f"SELECT * FROM Bookmark WHERE lower(title) = '{selected_link}'")
        link_change = input(f'Enter your new link here: ')
        mycursor.execute(f"UPDATE Bookmark SET link = '{link_change}' WHERE title = '{selected_link}'")
        db.commit()
        mycursor.execute(f"SELECT * FROM Bookmark WHERE link = '{link_change}'")
        updatedrecord = mycursor.fetchone()
        print(updatedrecord)
    elif field_update == 'c':
        print('You have selected to update a bookmark details!')
        selected_details = input(f'Enter the TITLE of the bookmark details you want to update: ')
        mycursor.execute(f"SELECT * FROM Bookmark WHERE lower(title) = '{selected_details}'")
        details_change = input(f'Enter new details information here: ')
        mycursor.execute(f"UPDATE Bookmark SET details = '{details_change}' WHERE title = '{selected_details}'")
        db.commit()
        mycursor.execute(f"SELECT * FROM Bookmark WHERE details = '{details_change}'")
        updatedrecord = mycursor.fetchone()
        print(updatedrecord)
    else :
        print("Invalid input. Exiting...")
        exit()


def delete_bookmark():
    print('You have selected to delete a bookmark. ')
    delete_option = input(f'Enter the TITLE of the bookmark you want to update: ')
    mycursor.execute(f"SELECT * FROM Bookmark WHERE lower(title) = '{delete_option}'")
    confirm = input(f'Are you sure you want to delete this record? (y/n) ')

    if confirm == 'y':
        mycursor.execute(f"DELETE FROM Bookmark WHERE lower (title) = '{delete_option}'")
        db.commit()
        print(f"You have deleted '{delete_option}' from your table.")
    elif confirm  == 'n':
        print('Exiting...')
    else:
        print('Invalid input. Exiting...')

def display_all():
    mycursor.execute(f"SELECT title, link, details FROM Bookmark")
    all_bookmarks = mycursor.fetchall()
    print(all_bookmarks)
    


greet_user()

