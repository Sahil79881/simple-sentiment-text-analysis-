from textblob import TextBlob
import requests
from newspaper import Article

def fetch_text_from_url(url):
    try:
        
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except Exception as e:
        print("An error occurred:", e)
        return None

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    else:
        return "Neutral"

if __name__ == "__main__":
    url = input("Enter the URL: ")
    text = fetch_text_from_url(url)
    if text:
        result = analyze_sentiment(text)
        print("The sentiment of the page is:", result)

        

