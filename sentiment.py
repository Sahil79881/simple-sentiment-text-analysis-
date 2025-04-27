from textblob import TextBlob
import requests
from bs4 import BeautifulSoup

def fetch_text_from_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Get all text inside paragraph tags
            paragraphs = soup.find_all('p')
            text = ' '.join([para.get_text() for para in paragraphs])
            return text
        else:
            print("Failed to retrieve the webpage. Status code:", response.status_code)
            return None
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
        

