# import Python Dependencies
import urllib2
import json

# Setting the page_id of Expedia Facebook page
page_id = 'expedia'

# Access token for my FB page ---- Remember this is a temporary access_token this will expire after limited time
access_token = 'EAACEdEose0cBANJs0fHQeTb1jAff8sNXjk40v314kjw68uKFwIDZCukop9LLRFVZACVv5Mdu9EbBkxpgq0NZBT1O3v2rMZC2IJlXoLWfVW6KBsbxk5BzGusE2EabhTvu402WmZCEHYOGeyss3sX3eG7dousbELevntTkxmDrmdHFdZCSTAxLUtc3ZB22HonuftZCN5IZCg27n7AZDZD'

# app_id = '692373707621416'
# app_secret = <Secret Token>  # Generally should not be shared with anyone
# access_token = app_id + '|' + app_secret

def getFacebookPageData(page_id, access_token):
    # construct the URL string
    base = "https://graph.facebook.com/v2.4"
    node = "/" + page_id + "/posts"
    parameters = "/?access_token=%s" % access_token
    url = base + node + parameters

    # retrieve data
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    data = json.loads(response.read())

    # Getting Latest 8 posts from Expedia Facebook page
    limited = data['data'][:9]
    print data['data'][:9]
    with open('LatestPosts.json', 'w') as outfile:
        json.dump(limited, outfile)

getFacebookPageData(page_id, access_token)
