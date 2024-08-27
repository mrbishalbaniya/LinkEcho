import requests
from bs4 import BeautifulSoup
from argparse import ArgumentParser
import sys
import time

def banner():
    print(r""" \033[32m
 _     _       _    _____     _           
| |   (_)_ __ | | _| ____|___| |__   ___  
| |   | | '_ \| |/ /  _| / __| '_ \ / _ \ 
| |___| | | | |   <| |__| (__| | | | (_) |
|_____|_|_| |_|_|\_\_____\___|_| |_|\___/ \033[0m

\033[41m LinkEcho: Recursive URL Finder \033[0m\n\033[33m""")

def fetch_urls(url, max_depth, current_depth=0, visited=None):
    """
    Recursively fetch all URLs from the given URL up to the specified depth.

    Args:
        url (str): The URL of the web page to fetch.
        max_depth (int): The maximum depth of recursion.
        current_depth (int): The current depth of recursion (used internally).
        visited (set): A set of visited URLs to avoid duplication.

    Returns:
        set: A set of URLs found on the web page.
    """
    if visited is None:
        visited = set()

    if current_depth > max_depth:
        return visited

    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        links = set()

        for a in soup.find_all("a"):
            href = a.get("href")
            if href:
                href = requests.compat.urljoin(url, href)
                if href not in visited:
                    visited.add(href)
                    links.add(href)
                    # Recursively fetch URLs from this link
                    fetch_urls(href, max_depth, current_depth + 1, visited)
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")

    return visited

def parse_arguments():
    """Parse command-line arguments."""
    parser = ArgumentParser(description="LinkEcho: Find and list URLs from a web page with recursive search.")
    parser.add_argument("-u", "--url", help="URL to fetch", required=True)
    parser.add_argument("-d", "--depth", help="Maximum depth for URL recursion", type=int, default=1)
    parser.add_argument("-o", "--output", help="File to save results", type=str, default=None)
    return parser.parse_args()

def save_to_file(urls, file_path):
    """Save URLs to a file."""
    with open(file_path, "w") as file:
        for url in urls:
            file.write(f"{url}\n")

def main():
    # Display banners
    banner()

    # Parse command-line arguments
    args = parse_arguments()

    # Fetch URLs
    urls = fetch_urls(args.url, args.depth)
    urls = sorted(urls)

    # Display results
    print(f"\nFound {len(urls)} URL(s):")
    for url in urls:
        print(url)
        time.sleep(0.2)

    # Save results if output file is specified
    if args.output:
        save_to_file(urls, args.output)
        print(f"\nResults saved to {args.output}")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Error: the following arguments are required: -u/--url")
        sys.exit(1)
    main()
