import json
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

consumer_key = '9KHrtTbzWZtyEHsMK6RysWSvy'
consumer_secret = 'hWJXiqe3Pxf7fxLeg7GbyGldyHKva7A49PNMwFntZe7vb3ocxe'
access_token = '98808847-rXCvDK0lUBcnHPXu3kFXfs4zl2puvYj4pRgFOZGg5'
access_secret = '19yYGloF7gojnF2KdI5TGS4L0SRfzvD13fBfN76TDsCQb'

news_handles = {
    'timesofinda': 'toi'
}

def replace_mentions(text, j):
    for mention in j['entities']['user_mentions']:
        text = text.replace('@' + mention['screen_name'], mention['name'])
    return text

def process_tweet(j):
    """
    returns: {
        'text':,
        'time':,
        'channel': 'DB Id of the channel'
    }
    """
    if j.get('created_at') and not j.has_key('retweeted_status'):
        ms = j['timestamp_ms']
        user = j['user']['screen_name']
        t = j['text']

        t = replace_mentions(t, j)

        return {
            'text': t,
            'time': int(ms)/1000,
            'channel': news_handles[user]
        }

    return None


class ToiListener(StreamListener):

    def on_data(self, data):
        j = json.loads(data)
        tweet = process_tweet(j)
        return True

    def on_error(self, status):
        print status


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

ids = [str(tweepy.API(auth).get_user(news_handle).id) for news_handle in news_handles.keys()]
if len(ids) == 0:
    ids = None

twitter_stream = Stream(auth, ToiListener())
twitter_stream.filter(follow=ids)
