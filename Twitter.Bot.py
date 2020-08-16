import tweepy
import time
import logging
# from TwitterFollowBot import TwitterBot
# from decouple import config

# AK : Mxa46NO2MVK0mqWRYLWLDPWYn (KumavatVijay11) / 9j0ZRpfoIFfsrlT7T1ra4s10r  (kvm3coder)
# AKS : jdajgdFI10DGtmQR3NxOHW8a7IboXPZ17KmrW6Ok4ZvggWS98N (KumavatVijay11) / FMjyz6N7ftHxrb2gKBrATGw93QHlhBYEDH2tmOQBa6nAzMUHve (kvm3coder)
# AT: 1013002626311471104-ARs9yVeK2Bt17tdRRFLkIGQbdXfo3E (KumavatVijay11) / 1294668148801593344-68sDi6MkTUaNKCwWGAKipk7cQLCHtf (kvm3coder)
# ATS : By93rwR8R0fT8UG77clnCCZMqBPPEfMZoqillRreZ3TJt (KumavatVijay11) / E6PEjHGZM6b3KRToZT9FePfMQ2zM92LZh6eTblTlY3kvs (kvm3coder)

# Authenticate to Twitter
consumer_key = 'Mxa46NO2MVK0mqWRYLWLDPWYn'
consumer_secret = 'jdajgdFI10DGtmQR3NxOHW8a7IboXPZ17KmrW6Ok4ZvggWS98N'
key = '1013002626311471104-ARs9yVeK2Bt17tdRRFLkIGQbdXfo3E'
secret = 'By93rwR8R0fT8UG77clnCCZMqBPPEfMZoqillRreZ3TJt'

# Create API object
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(key,secret)

api=tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

user=api.me()

# # Create a tweet
# api.update_status("Hello Tweepy")

# Automatic like post from hashtag
hashtag = '#India'
nrTweets=3

print("")
print('"Automatic like post from hashtag"')
print("")
for tweet in tweepy.Cursor(api.search,hashtag).items(nrTweets):
    try:
        print('Tweet Liked 😉')
        tweet.favorite()
        time.sleep(2)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

# Automatic like post from username
username = 'kvm3coder'
nrTweets=3

print("")
print('"Automatic like post from username"')
print("")
for tweet in tweepy.Cursor(api.search,username).items(nrTweets):
    try:
        print('Tweet Liked')
        tweet.favorite()
        time.sleep(2)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

# # Retweet
# hashtag = "#WatchKhudaHaafiz"
# tweetNumber = 10

# tweets = tweepy.Cursor(api.search, hashtag).items(tweetNumber)

# def searchBot():
#     for tweet in tweets:
#         try:
#             tweet.retweet()
#             #tweet.like()
#             print("Retweet is Done !!!")
#             time.sleep(2)
#         except tweepy.TweepError as e:
#             print(e.reason)
#             time.sleep(2)
        
# searchBot()

# username, followers count, following count and followers username
print("")
print('"Print the username, followers count, following count and followers username"')
print("")
print(user.screen_name)
print("")
print("Followers : ",user.followers_count)
print("Following : ",user.friends_count)
print("")
for follower in user.followers():
    print(follower.name)

print("")
print('"follow the your followers"')


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# follow the your followers
def follow_followers(api):
    logger.info("Retrieving and following followers")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            try:
                follower.follow()
                logger.info(f"Following {follower.name}")
            except tweepy.error.TweepError:
                pass

follow_followers(api)

#unfollow the any your followers
# def unfollow(api, follower_id = None):
#     if not follower_id:
#         logger.info("Retrieving current users being followed...")
#         for following_id in tweepy.Cursor(api.friends).items():
#             try:
#                 api.destroy_friendship(following_id.id)
#                 logger.info(f"Unfollowed {following_id.name}")
#             except tweepy.error.TweepError:
#                 pass
#     else:
#         try:
#             api.destroy_friendship(follower_id)
#             logger.info(f"Unfollowed {follower_id}...")
#         except tweepy.error.TweepError:
#             pass

# unfollow(api, "@Bhavesh Maratha")

# # show the your followers
# def main():
#     users=tweepy.Cursor(api.followers,screen_name="KumavatVijay11",count=1000).items()
#     for i in range(0,11):
#         try:
#             user=next(users)
#             print(user.screen_name)
#             print(user.name)
#         except tweepy.TweepError:
#             print("Tweepy has hit  its rate limit for now")
#             time.sleep(10)
#             next(users)

# main()