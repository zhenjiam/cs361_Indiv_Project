# -----------------------------------------------------------
# BASIC FUNCTIONS: ADD item, EDIT item, DELETE item
def add(dict, to_add, str1, w_name=None, str2=None, c_name=None):
    e_name = None
    if to_add == "world":
        dict[str1] = [str2, {}]    # print {world:[None, {}]}
        w_name = str1
    elif to_add == "category":
        dict[w_name][1][str1] = None # print {world:[overview, {category:None}]}
        c_name = str1
    elif to_add == "entry":
        dict[w_name][1][c_name][str1] = str2 # print {world:[overview, {category: {entry:None}}]}
        e_name = str1
    return w_name, c_name, e_name

def edit(dict, page, new_str, w_name=None, choice=None, old_str= None, c_name=None, e_name=None):
    if page == "world" and choice == "E":
        dict[new_str] = dict[old_str]
        del dict[old_str]
        w_name = new_str
    elif page == "world" and choice == "Z":
        dict[w_name][0] = new_str
    elif page == "category":
        dict[w_name][1][new_str] = dict[w_name][1][old_str]
        del dict[w_name][1][old_str]
        c_name = new_str
    elif page == "entry" and choice == "E":
        dict[w_name][1][c_name][new_str] = dict[w_name][1][c_name][old_str]
        del dict[w_name][1][c_name][old_str]
        e_name = new_str
    elif page == "entry" and choice == "T":
        dict[w_name][1][c_name][e_name] = new_str
    return w_name, c_name, e_name

def delete(dict, page, deleting, w_name=None, c_name=None):
    if page == "home":
        del dict[deleting]
    elif page == "world":
        del dict[w_name][1][deleting]
    elif page == ("category" or "entry"):
        del dict[w_name][1][c_name][deleting]
        page = "category"
    return page, w_name, c_name






















