# -----------------------------------------------------------
# MAIN: PUT PROGRAM TO WORK
from BasicFunc import *
from Pages import *

def make_choices(dict, choice, page, add_delete, w_name, c_name=None, e_name=None):
    if choice == "A":
        if page == "home":
            str1 = input("Input world name: ")
            str2 = input("Input world overview: ")
            w_name, c_name, e_name = add(dict, add_delete, str1, None, str2)
        if page == "world":
            str1 = input("Input category name: ")
            w_name, c_name, e_name = add(dict, add_delete, str1, w_name)
        if page == "category":
            str1 = input("Input entry name: ")
            str2 = input("Input entry text: ")
            w_name, c_name, e_name = add(dict, add_delete, str1, w_name, str2, c_name)
    elif choice == "E":
        old_str = input("Choose %s to edit:  " % page)
        new_str = input("Input new %s: " % page)
        w_name, c_name, e_name = edit(dict, page, new_str, w_name, choice, old_str, c_name, e_name)
    elif choice == "Z":
        new_str = input("Input new overview: ")
        w_name, c_name, e_name = edit(dict, page, new_str, w_name, choice)
    elif choice == "T":
        new_str = input("Input new text: ")
        w_name, c_name, e_name = edit(dict, page, new_str, w_name, choice, None, c_name, e_name)
    elif choice == "D":
        deleting = input("Choose %s to delete:  " % add_delete)
        confirm = input("Are you sure you want to delete %s? Enter 'Y' to confirm: " % add_delete)
        if confirm == "Y":
            page, w_name, c_name = delete(dict, add_delete, deleting, w_name, c_name)
        else:
            return
    return page, w_name, c_name, e_name

def generate_page(dict, curr_page, item, choice=None, w_name=None, c_name=None, e_name = None):
    if choice == "G":
        goal = input("Choose a %s: " % item)
        if item == "world" and goal in dict:
            curr_page, item, w_name = worldpage(dict, goal)
        elif item == "category" and goal in dict[w_name]:
            curr_page, item, w_name, c_name = categorypage(dict, w_name, goal)
        elif item == "entry" and goal in dict[w_name][1][c_name]:
            curr_page, item, w_name, c_name, e_name = entrypage(dict, w_name, c_name, goal)
    elif choice == "R":
        curr_page, item = homepage(dict)
    elif choice == "W":
        curr_page, item, w_name = worldpage(dict, w_name)
    elif choice == "C":
        curr_page, item, w_name, c_name = categorypage(dict, w_name, c_name)
    else:
        if curr_page == "home":
            curr_page, item = homepage(dict)
        elif curr_page == "world":
            curr_page, item, w_name = worldpage(dict, w_name)
        elif curr_page == "category":
            curr_page, item, w_name, c_name = categorypage(dict, w_name, c_name)
        elif curr_page == "entry":
            curr_page, item, w_name, c_name, e_name = entrypage(dict, w_name, c_name, e_name)
    return curr_page, item, w_name, c_name, e_name




