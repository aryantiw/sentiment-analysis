import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


consumer_key = 'UqHRhFlJ7KXj5onzKFkdUI9uq'
consumer_secret = 'm7xO2XlzuyuQ7gQtvwKz4d7weZIl0Zs0KiRrakRjzCaQoUzkgK'
access_token = '1487411554215555072-6ou3xZf8SB3KIOYbzz4R1RjYiy73Z1'
access_secret = 'UibHIscgD3o8TRXJ8DfPUC3Yu02ENKkj5cSPKtbMXNOkc'



class StdOutListener(StreamListener):

    def on_data(self, data):
        with open('data/tweetdata.txt','a') as tf:
            tf.write(data)
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':


    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    stream = Stream(auth, l)

    stream.filter(track=['depression', 'anxiety', 'mental health', 'suicide', 'stress', 'sad'])