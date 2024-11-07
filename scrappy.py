import requests
from bs4 import BeautifulSoup
import argparse
import os
from datetime import datetime

def fetch_proxies(url):
    try:
        # Set a user-agent to mimic a browser request
        headers = {
            'User -Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text
    except requests.RequestException as e:
        print(f"An error occurred while fetching the URL: {e}")
        return None

def parse_proxies(html):
    soup = BeautifulSoup(html, 'html.parser')
    proxies = []

    # Try to find the table with proxies
    proxy_table = soup.find('table', {'id': 'proxylisttable'})
    
    # If not found, try to get the first table on the page
    if proxy_table is None:
        print("Proxy table not found by ID. Attempting to find the first table on the page.")
        proxy_table = soup.find('table')

    if proxy_table:
        for row in proxy_table.tbody.find_all('tr'):
            columns = row.find_all('td')
            if columns:
                ip = columns[0].text.strip()
                port = columns[1].text.strip()
                proxies.append(f"{ip}:{port}")
    else:
        print("No proxy table found on the page.")

    return proxies

def save_proxies(proxies, filename):
    try:
        with open(filename, "w") as file:
            for proxy in proxies:
                file.write(f"{proxy}\n")  # Write each proxy on a new line
        print(f"Proxies have been saved to {filename}.")
    except IOError as e:
        print(f"An error occurred while saving proxies: {e}")

def generate_default_filename(url):
    # Generate a default filename based on the current timestamp and the URL
    base_name = url.split("//")[-1].split("/")[0]  # Extract the domain from the URL
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{base_name}_{timestamp}_proxies.txt"

def main():
    parser = argparse.ArgumentParser(description='Scrape proxies from a website.')
    parser.add_argument('url', type=str, help='The URL of the proxy list website')
    parser.add_argument('--output', type=str, help='The output filename for saving proxies (default: generated based on URL)', default=None)

    args = parser.parse_args()

    html = fetch_proxies(args.url)
    if html:
        proxies = parse_proxies(html)
        if proxies:
            output_filename = args.output if args.output else generate_default_filename(args.url)
            save_proxies(proxies, output_filename)
        else:
            print("No proxies found.")
    else:
        print("Failed to fetch the HTML content.")

if __name__ == "__main__":
    main()