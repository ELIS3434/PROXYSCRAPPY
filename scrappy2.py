import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime
import random
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# List of user agents for rotation
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
    'Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Mobile Safari/537.36'
]

# Predefined list of URLs to scrape
PROXY_SITES = [
    'https://www.free-proxy-list.net/',
    'https://www.us-proxy.org/',
    # Add more proxy sites here if needed
]

def fetch_proxies(url):
    try:
        headers = {
            'User -Agent': random.choice(USER_AGENTS)
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text
    except requests.RequestException as e:
        logging.error(f"An error occurred while fetching the URL {url}: {e}")
        return None

def parse_proxies_from_free_proxy_list(html):
    soup = BeautifulSoup(html, 'html.parser')
    proxies = []
    proxy_table = soup.find('table', {'id': 'proxylisttable'})

    if proxy_table:
        for row in proxy_table.tbody.find_all('tr'):
            columns = row.find_all('td')
            if columns:
                ip = columns[0].text.strip()
                port = columns[1].text.strip()
                proxies.append(f"{ip}:{port}")
    else:
        logging.warning("No proxy table found on free-proxy-list.net.")
    
    return proxies

def parse_proxies_from_us_proxy(html):
    soup = BeautifulSoup(html, 'html.parser')
    proxies = []
    proxy_table = soup.find('table', {'class': 'table'})

    if proxy_table:
        for row in proxy_table.find_all('tr'):
            columns = row.find_all('td')
            if columns:
                ip = columns[0].text.strip()
                port = columns[1].text.strip()
                proxies.append(f"{ip}:{port}")
    else:
        logging.warning("No proxy table found on us-proxy.org.")
    
    return proxies

def parse_proxies(html, url):
    # Determine the parsing function based on the URL
    if 'free-proxy-list.net' in url:
        return parse_proxies_from_free_proxy_list(html)
    elif 'us-proxy.org' in url:
        return parse_proxies_from_us_proxy(html)
    else:
        logging.warning(f"No parser available for {url}.")
        return []

def save_proxies(proxies, filename):
    try:
        with open(filename, "w") as file:
            for proxy in proxies:
                file.write(f"{proxy}\n")  # Write each proxy on a new line
        logging.info(f"Proxies have been saved to {filename}.")
    except IOError as e:
        logging.error(f"An error occurred while saving proxies to {filename}: {e}")

def generate_default_filename(url):
    base_name = url.split("//")[-1].split("/")[0]  # Extract the domain from the URL
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{base_name}_{timestamp}_proxies.txt"

def main():
    all_proxies = []

    for url in PROXY_SITES:
        logging.info(f"Fetching proxies from: {url}")
        html = fetch_proxies(url)
        if html:
            proxies = parse_proxies(html, url)
            if proxies:
                all_proxies.extend(proxies)
                output_filename = generate_default_filename(url)
                save_proxies(proxies, output_filename)
            else:
                logging.warning(f"No proxies found at {url}.")
        else:    
                logging.error (f"Failed to fetch the HTML content from {url}.")

    # Optionally save all proxies to a single file
    if all_proxies:
        combined_output_filename = "combined_proxies.txt"
        save_proxies(all_proxies, combined_output_filename)

if __name__ == "__main__":
    main()