
# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from firebase import firebase

# Variables that contains the user credentials to access Twitter API
access_token = "546077366-whwABXIlnpGiQq4uD1bVKDZIfl2fk47beJZD0kXM"
access_token_secret = "1IBBlHSwYxGdWiKUgxcrb6w3yxIXhWuVIHUOQF04WLREm"
consumer_key = "fvIvqMiBD4nyIJBZESvGfBKxC"
consumer_secret = "ex1sUrdHYktlLqmuzv08YYuLbIgyVYSowkyAW1vuTmlWho4Bjj"


# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    def on_data(self, data):
        print data
        firebase1 = firebase.FirebaseApplication('https://mydd-d1223.firebaseio.com/', None)
        result = firebase1.post('/tweets',data)
        print result

        return True

    def on_error(self, status):
        firebase1 = firebase.FirebaseApplication('https://mydd-d1223.firebaseio.com/', None)
        result = firebase1.post()
        print result
        print "status: " + status


if __name__ == '__main__':
    # This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    # This line filter Twitter Streams to capture data by the keywords
    stream.filter(track=['#bloodrequest'])

