import praw
import requests

from pushbullet import Pushbullet
pb = Pushbullet("enter your api key here")

requests.packages.urllib3.disable_warnings()
r = praw.Reddit(user_agent="Today_I_Learned_applicaton")
submissions = r.get_subreddit("todayilearned").get_hot(limit=2)
TopPost = ""
firstTime = False

for x in submissions:
   if( not firstTime):
        firstTime = True
        continue 
   TopPost = x.title
push = pb.push_note("Top post from Today I learned!" , TopPost)
