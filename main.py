import praw
import pdb
import re
import os
from praw.models import MoreComments


# reddit = praw.Reddit('tyvc_bot', user_agent='bot2 user agent')
reddit = praw.Reddit('tyvc_bot')
subreddit = reddit.subreddit('pewdiepiesubmissions')

# if not os.path.isfile("posts_replied_to.txt"):
#     posts_replied_to = []

# else:
#     with open("posts_replied_to.txt", "r") as f:
#        posts_replied_to = f.read()
#        posts_replied_to = posts_replied_to.split("\n")
#        posts_replied_to = list(filter(None, comments_replied_to))
#        #removes blank entries

if not os.path.isfile("comments_replied_to.txt"):
    comments_replied_to = []

else:
    with open("comments_replied_to.txt", "r") as f:
       comments_replied_to = f.read()
       comments_replied_to = comments_replied_to.split("\n")
       comments_replied_to = list(filter(None, comments_replied_to))
       #removes blank entries
       
for submission in subreddit.hot(limit=10):
  for comment in submission.comments:
    if isinstance(comment, MoreComments):
        continue
    if re.search("!cool", comment.body, re.IGNORECASE):
      comment.reply("Thank you /u/%s, very cool!" % (submission.author.name))
      print("Bot replying to : ", comment.body)
      comments_replied_to.append(comment.id)

with open("comments_replied_to.txt", "w") as f:
    for comment_id in comments_replied_to:
      f.write(comment_id + "\n")
