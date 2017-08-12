
# Import the necessary methods from tweepy library
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from firebase import firebase

import ast

# Variables that contains the user credentials to access Twitter API
access_token = "546077366-whwABXIlnpGiQq4uD1bVKDZIfl2fk47beJZD0kXM"
access_token_secret = "1IBBlHSwYxGdWiKUgxcrb6w3yxIXhWuVIHUOQF04WLREm"
consumer_key = "fvIvqMiBD4nyIJBZESvGfBKxC"
consumer_secret = "ex1sUrdHYktlLqmuzv08YYuLbIgyVYSowkyAW1vuTmlWho4Bjj"


# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
#    def on_status(self, data):

    def on_data(self, data):
        #data = ast.literal_eval(data)

        json_string = json.loads(data)

        firebase1 = firebase.FirebaseApplication('https://mydd-d1223.firebaseio.com/', None)
        result = firebase1.post('/tweets', json_string)
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':
    # This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    # This line filter Twitter Streams to capture data by the keywords
    stream.filter(track=['#bloodrequest'])




# {"created_at":"Sat Aug 12 01:04:05 +0000 2017","id":896175421070299136,"id_str":"896175421070299136","text":"fgfg #bloodrequest","source":"\u003ca href=\"http:\/\/twitter.com\" rel=\"nofollow\"\u003eTwitter Web Client\u003c\/a\u003e","truncated":false,"in_reply_to_status_id":null,"in_reply_to_status_id_str":null,"in_reply_to_user_id":null,"in_reply_to_user_id_str":null,"in_reply_to_screen_name":null,"user":{"id":546077366,"id_str":"546077366","name":"Christine Tee","screen_name":"PyTeeChristine","location":"Kuala Lumpur","url":"http:\/\/www.christinetee.com","description":"Google Student Ambassador 13\/14","protected":false,"verified":false,"followers_count":105,"friends_count":323,"listed_count":8,"favourites_count":23,"statuses_count":609,"created_at":"Thu Apr 05 15:56:13 +0000 2012","utc_offset":28800,"time_zone":"Kuala Lumpur","geo_enabled":true,"lang":"en","contributors_enabled":false,"is_translator":false,"profile_background_color":"000000","profile_background_image_url":"http:\/\/pbs.twimg.com\/profile_background_images\/597719900610695169\/mo_M-lrM.jpg","profile_background_image_url_https":"https:\/\/pbs.twimg.com\/profile_background_images\/597719900610695169\/mo_M-lrM.jpg","profile_background_tile":false,"profile_link_color":"ABB8C2","profile_sidebar_border_color":"000000","profile_sidebar_fill_color":"000000","profile_text_color":"000000","profile_use_background_image":true,"profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/648183911785172992\/6ti8YDHP_normal.jpg","profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/648183911785172992\/6ti8YDHP_normal.jpg","profile_banner_url":"https:\/\/pbs.twimg.com\/profile_banners\/546077366\/1500610692","default_profile":false,"default_profile_image":false,"following":null,"follow_request_sent":null,"notifications":null},"geo":null,"coordinates":null,"place":{"id":"7b02fbddf4d9f2c6","url":"https:\/\/api.twitter.com\/1.1\/geo\/id\/7b02fbddf4d9f2c6.json","place_type":"city","name":"Kuala Lumpur City","full_name":"Kuala Lumpur City, Kuala Lumpur Federal Territory","country_code":"MY","country":"Malaysia","bounding_box":{"type":"Polygon","coordinates":[[[101.668232,3.104906],[101.668232,3.192155],[101.742378,3.192155],[101.742378,3.104906]]]},"attributes":{}},"contributors":null,"is_quote_status":false,"retweet_count":0,"favorite_count":0,"entities":{"hashtags":[{"text":"bloodrequest","indices":[5,18]}],"urls":[],"user_mentions":[],"symbols":[]},"favorited":false,"retweeted":false,"filter_level":"low","lang":"tr","timestamp_ms":"1502499845174"}
