#Adapted from https://github.com/shantnu/RedditBot/blob/master/Part2/reply_post.py
#Changes made by: DillTice
#!/usr/bin/python
import praw
import pdb
import re
import os

rick_quote = ["To be fair, you have to have a very high IQ to understand Rick and Morty. The humour is extremely subtle, and without a solid grasp of theoretical physics most of the jokes will go over a typical viewer’s head. There’s also Rick’s nihilistic outlook, which is deftly woven into his characterisation- his personal philosophy draws heavily from Narodnaya Volya literature, for instance. The fans understand this stuff; they have the intellectual capacity to truly appreciate the depths of these jokes, to realise that they’re not just funny- they say something deep about LIFE. As a consequence people who dislike Rick & Morty truly ARE idiots- of course they wouldn’t appreciate, for instance, the humour in Rick’s existential catchphrase “Wubba Lubba Dub Dub,” which itself is a cryptic reference to Turgenev’s Russian epic Fathers and Sons. I’m smirking right now just imagining one of those addlepated simpletons scratching their heads in confusion as Dan Harmon’s genius wit unfolds itself on their television screens. What fools.. how I pity them."]

# Create the Reddit instance
reddit = praw.Reddit('bot1')

# Have we run this code before? If not, create an empty list
#if not os.path.isfile("comments_replied_to.txt"):
#comments_replied_to = []

# If we have run the code before, load the list of posts we have replied to
#else:
# Read the file into a list and remove any empty values
#with open("comments_replied_to.txt", "r") as f:
#comments_replied_to = f.read()
#comments_replied_to = comments_replied_to.split("\n")
#comments_replied_to = list(filter(None, comments_replied_to))

# Crawl the subreddit
subreddit = reddit.subreddit('funny')
for submission in subreddit.hot (limit=50):
    #Print submission title
    try:
        print("Title: **",submission.title,"**")
    except UnicodeEncodeError:
        #Seriously fuck these emojis
        print("Emojis are the devil**")
        pass
    #Iterate over all top level comments for the submission
    for top_level_comment in submission.comments:
        try:
            #if top_level_comment.link_id not in comments_replied_to:
                if re.search("morty", top_level_comment.body, re.IGNORECASE):
                    # Reply to the post
                    submission.reply(rick_quote)
                    # Store the current id into our list
                    comments_replied_to.append(submission.id)
                    
                    print("Replying to: ", top_level_comment.body, "\n")
        except UnicodeEncodeError:
            #Fucking emojis man...
            pass 
        except Exception as e:
            print(e)
    print("\n")
# Write our updated list back to the file
#with open("comments_replied_to.txt", "w") as f:
    #for comment_id in comments_replied_to:
        #f.write(comment_id + "\n")