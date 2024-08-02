import requests
from bs4 import BeautifulSoup
import csv
import logging

# Setup logging
logging.basicConfig(filename='web_scraper.log', level=logging.INFO,
					format='%(asctime)s:%(levelname)s:%(message)s')


def fetch_html(url):
	"""Fetch HTML content from a given URL."""
	try:
		response = requests.get(url)
		response.raise_for_status()
		logging.info(f"Successfully fetched URL: {url}")
		return response.text
	except requests.RequestException as e:
		logging.error(f"Error fetching URL: {url} - {e}")
		return None


def parse_html(html):
	"""Parse HTML to extract titles and summaries."""
	soup = BeautifulSoup(html, 'html.parser')
	articles = []
	for article in soup.find_all('article'):
		title = article.find('h1').get_text(strip=True)
		summary = article.find('p').get_text(strip=True)
		articles.append({'title': title, 'summary': summary})
	logging.info("Successfully parsed HTML content")
	return articles


def save_to_csv(data, filename):
	"""Save data to a CSV file."""
	try:
		with open(filename, mode='w', newline='', encoding='utf-8') as file:
			writer = csv.DictWriter(file, fieldnames=['title', 'summary'])
			writer.writeheader()
			writer.writerows(data)
		logging.info(f"Data successfully saved to {filename}")
	except IOError as e:
		logging.error(f"Error saving data to CSV: {e}")


def main():
	url = 'https://example-blog.com'
	html_content = fetch_html(url)
	if html_content:
		articles = parse_html(html_content)
		save_to_csv(articles, 'articles.csv')


if __name__ == '__main__':
	main()
