
from twitterfuncs import find_user, get_followers, find_hashtag, friends_of_friends


def test_find_user():
    first = find_user('@GA')
    second = find_user('GA')
    third = find_user('sdlkfjsfewjclmfocmeijc')
    fourth = find_user('GA', keys=['scrinname'])
    fifth = find_user('@GA', keys=['name', 'screen_name', 'followers_count', 'friends_count'])
    users = [first, second, third, fourth, fifth]

    return users

def test_find_hashtag():
    ds = find_hashtag('#DataScience')
    ds_no = find_hashtag('DataScience')
    ds_100 = find_hashtag('#DataScience', count=100)
    ds_recent = find_hashtag('#DataScience', search_type='recent')
    hashtags = [ds, ds_no, ds_100, ds_recent]
    
    return  hashtags

def test_get_followers():
    ga_at = get_followers('@GA')
    ga_no = get_followers('GA')
    ga_keys = get_followers('GA', keys=['name', 'followers_count'])
    ga_keysdf = get_followers('GA', keys=['name', 'followers_count'], to_df=True)
    ga_df = get_followers('GA', to_df=True)
    gfollow = [ga_at, ga_no, ga_keys, ga_keysdf, ga_df]

    return gfollow

def test_friends_of_friends():
    fof = friends_of_friends(['Beyonce', 'MariahCarey'])
    fof_df = friends_of_friends(['@Beyonce', '@MariahCarey'], to_df=True)
    fof_keys = friends_of_friends(['Beyonce', 'MariahCarey'], keys=['id', 'name'])
    fof_keysdf = friends_of_friends(['Beyonce', 'MariahCarey'], keys=['id', 'name'], to_df=True)
    fofs = [fof, fof_df, fof_keys, fof_keysdf]
    
    return fofs
    
def test_friends_of_friends_cursoring():
    fof = friends_of_friends(['Beyonce', 'MariahCarey'], full_search=True)
    fof_df = friends_of_friends(['@Beyonce', '@MariahCarey'], to_df=True, full_search=True)
    fof_keys = friends_of_friends(['Beyonce', 'MariahCarey'], keys=['id', 'name'],full_search=True)
    fof_keysdf = friends_of_friends(['Beyonce', 'MariahCarey'], keys=['id', 'name'], to_df=True, full_search=True)
    fofs = [fof, fof_df, fof_keys, fof_keysdf]
    
    return fofs


# if __name__ == '__main__':
#     finduser = test_find_user()
#     findhash = test_find_hashtag()
#     getflwers = test_get_followers()
#     foftest = test_friends_of_friends()
#     fofcursortest = test_friends_of_friends_cursoring()


    