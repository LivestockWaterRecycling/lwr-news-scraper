"""
lwr_news_scraper.py
-------------------
Script to Fetch and Save News Articles from the Livestock Water Recycling Website

This script fetches news articles from the specified URL and saves them in a JSON format.
It demonstrates basic usage of requests and BeautifulSoup for web scraping, and provides
a structured approach to parsing and saving data.

Author: Oscar Jaimes
Date: 2024-02-28
"""

import requests
import logging
import json
from bs4 import BeautifulSoup
from typing import List, Dict, Optional

NEWS_URL = 'https://www.livestockwaterrecycling.com/newsroom/featured/'
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_news(url: str) -> Optional[requests.Response]:
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response
    except requests.RequestException as e:
        logging.error(f"Failed to retrieve the webpage: {e}")
        return None

def parse_news(response: requests.Response) -> List[Dict[str, str]]:
    soup = BeautifulSoup(response.text, 'html.parser')
    html_articles = soup.find_all(class_='uk-panel uk-panel-space uk-width-1-1')
    formatted_articles = []

    for article in html_articles:
        title = article.find('h3').text.strip()
        content = article.find('div').text.strip()
        formatted_articles.append({
            'title': title,
            'content': content
        })

    return formatted_articles

def save_articles(articles: List[Dict[str, str]], filename: str = 'featured.json') -> None:
    try:
        with open(filename, 'w') as f:
            json.dump(articles, f, indent=4)
    except IOError as e:
        logging.error(f"Failed to save articles: {e}")

def main():
    logging.info("Starting news article fetch process")
    response = fetch_news(NEWS_URL)
    if response:
        articles = parse_news(response)
        save_articles(articles)
        logging.info("News articles fetched and saved successfully")

if __name__ == '__main__':
    main()
