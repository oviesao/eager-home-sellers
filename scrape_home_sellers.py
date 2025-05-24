import praw
import csv
from datetime import datetime

# Setting Reddit API creds
reddit = praw.Reddit(
    client_id="PQrKZwY-YbMuw7bskVUgg",
    client_secret="FTPi5sqj405yugkWu4GzBx39tMvzxw",
    user_agent="eager_home_seller_scraper by u/ifuharduhard"
)

# Define search terms
search_terms = ["selling my house", "house for sale", "home for sale", "fsbo", "moving need to sell"]

# Subreddits to target
subreddits = ["realestate", "fsbo", "homeowners", "personalfinance", "HomeImprovement"]

# Create a CSV file
filename = f"home_seller_leads_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
with open(filename, mode="w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["title", "url", "subreddit", "author", "created_utc", "score"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Searching of subreddits for posts containing the keywords
    for subreddit in subreddits:
        for term in search_terms:
            print(f"Searching '{term}' in r/{subreddit}")
            for post in reddit.subreddit(subreddit).search(term, limit=50):
                writer.writerow({
                    "title": post.title,
                    "url": post.url,
                    "subreddit": post.subreddit.display_name,
                    "author": str(post.author),
                    "created_utc": datetime.utcfromtimestamp(post.created_utc).strftime('%Y-%m-%d %H:%M:%S'),
                    "score": post.score
                })

print(f"\n✅ Scraping complete. Results saved in: {filename}")
