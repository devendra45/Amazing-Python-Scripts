import pyshortners

#url
url="https://hackerrank.com/contest/irjat/leaderboard"

# creating instance
short_url= pyshortners.Shortener()

# using tinyurl to shorten
print(short_url.tinyurl.short(url))
