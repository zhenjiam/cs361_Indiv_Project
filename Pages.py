# -----------------------------------------------------------
# SHOW PAGES: HOME, WORLD, CATEGORY, ENTRY

def homepage(dict):
    print("--------------HOME PAGE--------------")
    print("List of Worlds:")
    for key in dict:
        print(key)
    print()
    print("""Enter: 
    A - add new world         G - go to a world page    
    D - delete a world""")
    print("-------------------------------------")
    print(dict)
    return "home", "world"

def worldpage(dict, w_name):
    print("--------------%s--------------" % w_name)
    print("Overview:")
    print(dict[w_name])
    print()
    print("List of Categories:")
    if len(dict[w_name][1]) != 0:
        for key in dict[w_name][1]:
            print(key)
    print()
    print("""Enter: 
    E - edit world name       Z - edit overview      
    A - add new category      G - go to category page   
    D - delete a category     R - return to home page""")
    print("-------------------------------------")
    print(dict)
    return "world", "category", w_name


def categorypage(dict, w_name, c_name):
    print("--------------%s--------------" % c_name)
    print("List of Entries:")
    for key in dict[w_name][c_name]:
        print(key)
    print()
    print("""Enter: 
    E - edit category's name    A - add new entry 
    G - go to an entry          D - delete an entry
    W - return to world page    R - return to home page""")
    print("-------------------------------------")
    print(dict)
    return "category", "entry", w_name, c_name


def entrypage(dict, w_name, c_name, e_name):
    print("--------------%s--------------" % e_name)
    print("Text:")
    print(dict[w_name][c_name][e_name])
    print()
    print("""Enter: 
    E - edit entry name         T - edit an entry's text
    D - delete entry            C - return to category page
    W - return to world page    R - return to home page""")
    print("-------------------------------------")
    print(dict)
    return "entry", None, w_name, c_name, e_name
