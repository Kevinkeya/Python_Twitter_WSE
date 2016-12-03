import tweepy
import json
import sys

auth = tweepy.OAuthHandler('GjZRsAbdr3XBX6Rj9OPP0X0XS', 'CGjrMMZsOxm0o6mPW2iVAWNUvwcMnsg0IObA3bOfTYJpWI8JwH')
auth.set_access_token('633648013-FgmNsiKLzBCcvsM18FZfFy7KjZ49Zu3GlCcnGePd',
                      'hP22Hq81cxTNwTEd91h91ZrrpXT8A6KEAa6NYlhzQPyNf')
api = tweepy.API(auth)

# This is the listener, resposible for receiving data
class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        # # Twitter returns data in JSON format - we need to decode it first
        # decoded = json.loads(data)
        #
        # # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        # print('@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore')))
        # print('')
        # return True

        # print (data)
        parsed_json = json.loads(data)
        print(parsed_json['place']['bounding_box']['coordinates'])
        fi = open("/Users/keya/twitter/Schiphol.json", 'a')
        t_id = str(parsed_json['id_str'])
        t_co = str(parsed_json['place']['bounding_box']['coordinates'])
        fi.write(t_id + ' ' + t_co + '\n')
        fi.close()

        return True

    def on_error(self, status):
        print(status)







if __name__ == '__main__':
    l = StdOutListener()
    print
    "Showing all new tweets from Schiphol:"
    # There are different kinds of streams: public stream, user stream, multi-user streams
    # In this example follow #programming tag
    # For more details refer to https://dev.twitter.com/docs/streaming-apis
    stream = tweepy.Stream(auth, l)
    # stream.filter(track=['programming'])
    stream.filter(locations=[4.73,52.29,4.98,52.42])






