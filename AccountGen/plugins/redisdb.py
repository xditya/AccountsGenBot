#    AccountsGenBot
#    Copyright (C) 2021 xditya

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    See < https://github.com/xditya/AccountsGenBot/blob/master/LICENSE > 
#    for the license.

# basic stuff by @Arnab431

from .. import *

def str_to_list(text):  # Returns List
    return text.split(" ")
    
def list_to_str(list):  # Returns String
    str = ""
    for x in list:
        str += f"{x} "
    return str.strip()

def is_added(id):  # Take int or str with numbers only , Returns Boolean
    if not str(id).isdigit():
        return False
    users = get_all_users()
    if str(id) in users:
        return True
    else:
        return False

def add_user(id):  # Take int or str with numbers only , Returns Boolean
    id = str(id)
    if not id.isdigit():
        return False
    try:
        users = get_all_users()
        users.append(id)
        xdi.set("BOT_USERS", list_to_str(users))
        return True
    except Exception as e:
        print(f"./add_user : {e}")
        return False

def get_all_users():  # Returns List
    users = xdi.get("BOT_USERS")
    if users is None or users == '':
        return ['']
    else:
        return str_to_list(users)