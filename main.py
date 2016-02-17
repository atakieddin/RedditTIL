import praw
import requests
requests.packages.urllib3.disable_warnings()
r = praw.Reddit(user_agent="Today_I_Learned_applicaton")
submissions = r.get_subreddit("todayilearned").get_hot(limit=2)

firstTime = False
for x in submissions:
   if( not firstTime):
        firstTime = True
        continue 
   print(x.title)
