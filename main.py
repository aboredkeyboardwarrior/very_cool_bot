import praw
import re
import os

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
    if re.search("!cool", comment.body, re.IGNORECASE):
      comment.reply("Thank you /u/%s, very cool!" % (submission.author.name))
      print("Bot replying to : ", comment.body)
      comments_replied_to.append(comment.id)

with open("comments_replied_to.txt", "w") as f:
    for comment_id in comments_replied_to:
      f.write(comment_id + "\n")
