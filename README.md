# THABALSDE001

## Project Details:
In this project, I have collected latest posts Expedia's Official Facebook page(https://www.facebook.com/expedia/psots). I have used Facebook Graph API for extracting posts. To use the FB Graph API, a person must setup a Facebook Developers account and has to use eiher Access Token(Expires after some time - Can be regeneerated) or can use App ID(A new FB app in Developers site) and App Secret(This is the secret code given to the developer to access the Graph API). 

## Technology:
- **Python** - Python 2.7.12
- **Facebook Graph API** - An Facebook API to access it's Contents(https://developers.facebook.com/docs/graph-api/)

## Relavant Files:
- **ExpediaPosts.py** - This Python file extracts the Eight Latest Posts from Expedia's Facebook Page.
- **LatestPosts.json** - This is a JSON file containing the Eight Latest Posts from Expedia's Facebook Page, on running ExpediaPosts.py it generates this JSON file 

## Details about Access Token or APP ID & APP Secret:
As said in the Project details, One must have a Facebook Developers account to get the Access Token or APP ID & APP Secret. 
- **Access Token** - Go to https://developers.facebook.com/tools/explorer/ to get the new Access Token. This Access Token expires in 2 hours. To get the new Access Token, We request it again by clicking _Get Token_ button.    
- **APP ID and APP Secret** - If we want to have permanent access to the FB Graph API, we can use APP ID and APP Secret. Go to https://developers.facebook.com/ and On the right there is a section listed "My Apps" from which you can select an application to see its information. Make a new APP and get the APP ID and APP Secret details.

## How to Run:
- Get the _Access Token or App ID & App Secret_ from Facebook Developers site. 
- Download/Clone the files from the repository.
- Then go into the folder/directory in which the project is present.
- Open the ExpediaPosts.py, _edit the Access Token or App ID & App Secret accordingly_ and save the file.
- Open a terminal and type - **_python ExpediaPosts.py_**

## Results:
- After running _python ExpediaPosts.py_, we will get a JSON file with Latest Eight Expedia's Facebook posts.

## Miscellaneous: 
- **Instead of 8 Latest Facebook Posts, we can collect data for any number of Posts**
- **In addition to Posts, We can collect Post Comments, Reactions to Posts etc.**
- **We can also collect the media information like Pictures, Videos, Post Links etc.**

