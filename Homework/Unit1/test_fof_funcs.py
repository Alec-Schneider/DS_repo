import requests
import pandas as pd
from twitterfuncs import tokens, flwerlist


def friends_of_friends_search(names, keys=None, to_df=False, full_search=False):
    """
    parameters
    ------------
    names: list of length two
        list of two Twitter users to compare friends list with
    keys: list; default set to None
        list of keys to return for information about each user
    to_df: bool; default set to False
        returns a DataFrame object if set to True
    full_search: bool; default set to False
        if set to true, will cursor through all followers of the 
        users until there are no more, or api limit has been 
        exceeded

    return
    ------------
    list or DataFrame of data objects for each user that two Twitter
    users have in common
    """
    # assert that list contains only two users
    assert(not len(names) > 2) , 'Please enter only two users'
    # remove @ symbol if included
    names = [name.replace('@', '') for name in names]
    # get dict of user dicts for each name passed to function
    name_flws = {}
    # check to see if user wants a full search
    if full_search:
        # loop through each name requested by user
        for name in names:
            # initialize cursor
            cursor = -1
            try:
                # keep getting a request for more followers until cursor is 0
                while cursor:
                    # set search query to include cursor
                    search = 'screen_name=' + name + '&cursor=%s' % cursor
                    r = requests.get(flwerlist + search, auth=tokens)
                    # get request to return a dict that contains the list of user dicts in 'users'
                    user_dict = r.json()
                    # set the cursor to next cursor from last request
                    cursor = user_dict['next_cursor']
                    # check if name is already in dict, i
                    if not name in name_flws.keys():
                        name_flws[name] = [user_dict]
                    else:
                        name_flws[name].append(user_dict)
            except KeyError as e:
                print("Key Error", e)
                print(user_dict['errors'])
    else:    
        for name in names:
            search = 'screen_name=' + name
            r = requests.get(flwerlist + search, auth=tokens)
            name_flws[name] = [r.json()]       
    # Due to a issues with the api rate limit, the function will end here if
    # if follower information wasn't returned for each name requested
    assert (len(name_flws.keys()) == 2), 'Both names were not returned'
    # check to see if screen names exist
    errors = []
    for name in name_flws.keys():
        if 'errors' in name_flws[name][0].keys():
            errors.append('%s Error. %s.' % (name, name_flws[name][0]['errors']))
    if errors:
        for msg in errors:
            print(msg)
        return False

    # check for missing keys
    if keys:
        missing_keys = [key for key in keys if not key in name_flws[name][0]['users'][0].keys()]
        if missing_keys:
            print('The following keys are not in the user object :')
            for key in missing_keys:
                print(key)
            print('\nPlease try again')
            return False
     
    users_dict = {}
    for name, list_of_dicts in name_flws.items():
        # name and list of dicts containing list of user dicts
        # create dict of name: list of user dicts
        for d in list_of_dicts:
            for i in d['users']:
                if not name in users_dict.keys():
                    users_dict[name] = [i]
                else:
                    users_dict[name].append(i)

    
    # makes one whole flat list of user dicts from each name
    name1users = [user for user in users_dict[names[0]]]
    name2users = [user for user in users_dict[names[1]]]
    
    # loop through each item in each list to see if users exist in both lists
    fof_list = []
    for user1 in name1users:
        for user2 in name2users:
            if user1['id'] == user2['id']:
                fof_list.append(user1)
           
    # create a list of user dicts with only keys that were passed
    if keys:
        fof_list = [{key: user[key] for key in keys} for user in fof_list]

    if to_df:
        df = pd.DataFrame(fof_list)
        return df
    
    return fof_list


def friends_of_friends(names, keys=None, to_df=False):
    """
    parameters
    ------------
    names: list of length two
        list of two Twitter users to compare friends list with
    keys: list; default set to None
        list of keys to return for information about each user
    to_df: bool; default set to False
        returns a DataFrame object if set to True

    return
    ------------
    list or DataFrame of data objects for each user that two Twitter
    users have in common
    """
    # assert that list contains only two users
    assert(not (len(names) > 2 or len(names) < 2)) , 'Please enter only two users'
    # remove @ symbol if included
    names = [name.replace('@', '') for name in names]
    # get dict of user dicts for each name passed to function
    name_flws = {}
    for name in names:
        search = 'screen_name=' + name
        r = requests.get(flwerlist + search, auth=tokens)
        name_flws[name] = r.json()

    # check to see if screen names exist
    errors = []
    for name in name_flws.keys():
        if 'errors' in name_flws[name].keys():
            errors.append('%s Error. %s.' % (name, name_flws[name]['errors']))
    if errors:
        for msg in errors:
            print(msg)
        return False

    # check for missing keys
    if keys:
        missing_keys = [key for key in keys if not key in name_flws[name]['users'][0].keys()]
        if missing_keys:
            print('The following keys are not in the user object :')
            for key in missing_keys:
                print(key)
            print('\nPlease try again')
            return False

    # get list of dicts of users 
    users_dict = {key: users['users'] for key, users in name_flws.items()}

    # get list of dicts of users 
    fof_list = []
    for user1 in users_dict[names[0]]:
        for user2 in users_dict[names[1]]:
            if user1['id'] == user2['id']:
                user1['name']
                fof_list.append(user1)

    # create a list of user dicts with only keys that were passed
    if keys:
        fof_list = [{key: user[key] for key in keys} for user in fof_list]

    if to_df:
        df = pd.DataFrame(fof_list)
        return df
    
    return fof_list
