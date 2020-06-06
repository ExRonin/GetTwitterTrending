import json
import tweepy


class TwitterTrendingsAPI:
    
    """
       
	   Cara Pakai
        
        Change apiKey, apiSecretKey, accessToken, accessTokenSecret with your own Twitter Apps from https://developer.twitter.com
        
        Use this class
        
        api = TwitterAPI(woeId=23424846, limit=10)
        api.getTrending()
    """

    def __init__(self, woeId, limit):
        self.apiKey = "<YOUR_API_KEY>"
        self.apiSecretKey = "<YOUR_API_SECRET_KEY>"
        self.accessToken = "<YOUR_ACCESS_TOKEN>"
        self.accessTokenSecret = "<YOUR_ACCESS_TOKEN_SECRET>"
        self.woeId = woeId
        self.limit = limit

    def getApiAuth(self):
        auth = tweepy.OAuthHandler(self.apiKey, self.apiSecretKey)
        auth.set_access_token(self.accessToken, self.accessTokenSecret)
        return tweepy.API(auth)

    def getTrending(self):
        trends = self.getApiAuth().trends_place(self.woeId)
        trending = json.loads(json.dumps(trends, indent=1))
        return trending[0]["trends"][:self.limit]

