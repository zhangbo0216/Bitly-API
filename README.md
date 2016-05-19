# Bitly-API
In this program, I create a class to deal with Bitly API of /v3/user/link_save, /v3/user/link_history and /v3/user/clicks. 

User should install Python Requests before using it.

To install Python Requests, type pip install requests in terminal
$ pip install requests
To use this API client library in a program, user should type: 
from Bitly_API_Client import client_library
at the beginning of the program.
To initialize the class client_library, user should provide his Access Token. You can generate a developer access token from https://bitly.com/a/oauth_apps
Here’s an example:
My_client= client_library (ACCESS TOKEN)

I create the following functions to make user interact with the API easily:
set_token(self,access_token)
User may want to change the access token when using the API, and can reset the token through this method.

save_link(self,longUrl, title=None, note=None, private=None, 
user_ts=None,domain=None)
Saves a long URL as a Bitlink in a user's history, with optional pre-set metadata. (Also returns a short URL for that link.)
Details of each parameters can be found on http://dev.bitly.com/links.html#v3_user_link_save and are all set to None on default except longUrl


link_history(self, limit=None, offset=None, created_before=None, created_after=None, modified_after=None, expand_client_id=None, archived_optional=None, private_optional=None, user=None, exact_domain=None, root_domain=None, keyword=None, campaign_id=None, query=None)
Returns entries from a user's link history in reverse chronological order.
Details of each parameters can be found on http://dev.bitly.com/user_info.html#v3_user_link_history


link_click(self,unit=None,units=None,timezone=None,rollup=None,limit=None,unit_reference_ts=None,format=None)
Returns the aggregate number of clicks on all of the authenticated user's Bitlinks.
Details of each parameters can be found on http://dev.bitly.com/user_metrics.html#v3_user_clicks

Attention: The parameter of save_link, link_history and link_click should be either String or integer. All the Boolean variable should set as “true” for True and “false” for False

The returning of save_link, link_history and link_click is a Response object of Requests. It can be shown on different formats including text or json. However, it is still hard for user to use the data directly, so I provide the following functions:


get_latest_saved_longUrl(self)
return a string which is the last long URL the saved though this client

get_latest_saved_aggregate_link(self)
return a string which is the last aggregate link the saved though this client


get_latest_saved_link(self)
return a string which is the last link the saved though this client

get_all_link_history(self)
return a list of all the information of history of user’s link

get_all_clicks(self)
return a list of sum of clicks of all the user’s link

get_all_links(self)
return all links in user’s history

get_all_aggregate_links(self)
return all aggregate links in user’s history which is good for sharing

get_all_longUrl(self)
return all long url in user’s history

most_click_day(self)
return the starting day and the number of clicks which has the largest amount of clicks during that time
