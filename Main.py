from ChoiceResponse import *
from Pages import *

dict = {}
curr_page, item = homepage(dict)
choice = None
w_name = None
c_name = None
e_name = None

while True:
    choice = input("Enter your choice: ")
    if choice == ("A" or "E" or "D" or "Z" or "T"):
        curr_page, w_name, c_name, e_name = make_choices(dict, choice, curr_page, item, w_name, c_name, e_name)
        curr_page, item, w_name, c_name, e_name = generate_page(dict, curr_page, item, choice, w_name, c_name, e_name)
    elif choice == ("G" or "R" or "W" or "C"):
        curr_page, item, w_name, c_name, e_name = generate_page(dict, curr_page, item, choice, w_name, c_name, e_name)
    else:
        print("Invalid choice, please try again.")


