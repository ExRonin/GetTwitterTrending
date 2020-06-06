# Import custom twitter trendings API
from TwitterTrendingsAPI import TwitterTrendingsAPI

# Define WOEID
"""
More World of Earth Id : https://codebeautify.org/jsonviewer/f83352
Find WOEID by your self

"""

INDONESIA_WOE_ID = 23424846
UNITED_KINGDOM_WOE_ID = 23424975

# Define TwitterTrendingsAPI Object with Limit 10 Trendings
api = TwitterTrendingsAPI(woeId=INDONESIA_WOE_ID, limit=10)

# Get Trendings
trendings = api.getTrending()
print(trendings)

# Filter Trendings By Hashtag
trends = list()
for trend in trendings:
    getTrendName = trend["name"].strip("#")
    trends.append(getTrendName)
print(trends)
