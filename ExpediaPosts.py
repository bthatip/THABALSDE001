# import Python Dependencies
import urllib2
import json

# Setting the page_id of Expedia Facebook page
page_id = 'expedia'

# Access token for my FB page ---- Remember this is a temporary access_token this will expire after limited time
access_token = 'EAACEdEose0cBAKRjNwGjUpq3MP4kY8pJYynCRGFnWZB3dWGZB3VRJdoBfMZBxhuuhKYIMznTMIJMT8EFYYTgOi2yXG105mFpD06fMdLfVVMiZCTj54W3KDr8qk13E5khXCYrteIagZAYxZBeHr7SdTooGXuU991ZB2DN2jSJ4boLva3HseKToGdmmZB5OZA0lx16CHyNBGdlmQgZDZD'

# app_id = '692373707621416'
# app_secret = <Secret Token>  # Generally should not be shared with anyone
# access_token = app_id + '|' + app_secret

def getFacebookPageData(page_id, access_token):
    # Giving the Base URL for Facebook Graph API
    base = "https://graph.facebook.com/v2.4"
    node = "/" + page_id + "/posts"
    parameters = "/?access_token=%s" % access_token

    # Construct the URL string
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

# Calling the Function
getFacebookPageData(page_id, access_token)
