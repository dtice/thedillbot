import praw

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("pythonforengineers")

for submission in subreddit.hot(limit=5):
	print("Title: ", submission.title)
	print("Text: ", submission.selftext)
	print("Upboats: ", submission.score)
	print("---------------------------\n")
