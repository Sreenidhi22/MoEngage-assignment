# moengage-doc-analysis/scraper.py

import requests
from bs4 import BeautifulSoup
import json
import os
from dotenv import load_dotenv

# Load environment variables (e.g., for API keys, though not strictly needed for scraping)
load_dotenv()

def fetch_article_content(url: str) -> str:
    """
    Fetches and parses the main content from a given URL.
    This function tries to extract the most relevant text content.
    """
    try:
        response = requests.get(url, timeout=10) # Added timeout for robustness
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Prioritize finding common article content tags
        # Adjust these selectors based on actual MoEngage documentation HTML structure
        article_content = soup.find('article') or \
                          soup.find('main') or \
                          soup.find('div', class_='article-body') or \
                          soup.find('div', id='main-content') # Common ZenDesk help center ID

        if article_content:
            # Remove script and style tags to clean the content
            for script_or_style in article_content(['script', 'style', 'nav', 'footer', 'header', 'aside']):
                script_or_style.extract()
            # Get text, strip whitespace, and replace multiple newlines with single ones
            text = article_content.get_text(separator='\n', strip=True)
            return "\n".join(filter(None, text.splitlines())) # Remove empty lines
        else:
            print(f"Warning: No specific article content tag found for {url}. Extracting body text.")
            # Fallback to body text if article-specific content is not found, but try to clean
            for script_or_style in soup.body(['script', 'style', 'nav', 'footer', 'header', 'aside']):
                script_or_style.extract()
            text = soup.body.get_text(separator='\n', strip=True)
            return "\n".join(filter(None, text.splitlines()))

    except requests.exceptions.Timeout:
        print(f"Error fetching URL {url}: Request timed out.")
        return ""
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return ""
    except Exception as e:
        print(f"Error parsing content from {url}: {e}")
        return ""

if __name__ == "__main__":
    print("--- Scraper Script: Fetching and Extracting Article Content ---")

    # List of MoEngage documentation URLs to scrape
    urls_to_scrape = [
        "https://partners.moengage.com/hc/en-us/articles/9643917325460-Create-creatives",
        "https://help.moengage.com/hc/en-us/articles/28194279371668-How-to-Analyze-OTT-Content-Performance",
        # Add more URLs here as needed for broader testing
    ]

    extracted_articles_data = []

    for url in urls_to_scrape:
        print(f"\nFetching content from: {url}")
        content = fetch_article_content(url)
        if content:
            print(f"Successfully extracted content (first 200 chars): \n{content[:200]}...")
            extracted_articles_data.append({"url": url, "content": content})
        else:
            print(f"Failed to extract content for: {url}")
            extracted_articles_data.append({"url": url, "content": None, "error": "Content extraction failed"})

    # Save the extracted data to a JSON file
    output_filename = "extracted_articles_complete.json"
    with open(output_filename, 'w', encoding='utf-8') as f:
        json.dump(extracted_articles_data, f, indent=4, ensure_ascii=False)

    print(f"\n--- Extraction complete. Data saved to {output_filename} ---")# moengage-doc-analysis/scraper.py

import requests
from bs4 import BeautifulSoup
import json
import os
from dotenv import load_dotenv

# Load environment variables (e.g., for API keys, though not strictly needed for scraping)
load_dotenv()

def fetch_article_content(url: str) -> str:
    """
    Fetches and parses the main content from a given URL.
    This function tries to extract the most relevant text content.
    """
    try:
        response = requests.get(url, timeout=10) # Added timeout for robustness
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Prioritize finding common article content tags
        # Adjust these selectors based on actual MoEngage documentation HTML structure
        article_content = soup.find('article') or \
                          soup.find('main') or \
                          soup.find('div', class_='article-body') or \
                          soup.find('div', id='main-content') # Common ZenDesk help center ID

        if article_content:
            # Remove script and style tags to clean the content
            for script_or_style in article_content(['script', 'style', 'nav', 'footer', 'header', 'aside']):
                script_or_style.extract()
            # Get text, strip whitespace, and replace multiple newlines with single ones
            text = article_content.get_text(separator='\n', strip=True)
            return "\n".join(filter(None, text.splitlines())) # Remove empty lines
        else:
            print(f"Warning: No specific article content tag found for {url}. Extracting body text.")
            # Fallback to body text if article-specific content is not found, but try to clean
            for script_or_style in soup.body(['script', 'style', 'nav', 'footer', 'header', 'aside']):
                script_or_style.extract()
            text = soup.body.get_text(separator='\n', strip=True)
            return "\n".join(filter(None, text.splitlines()))

    except requests.exceptions.Timeout:
        print(f"Error fetching URL {url}: Request timed out.")
        return ""
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return ""
    except Exception as e:
        print(f"Error parsing content from {url}: {e}")
        return ""

if __name__ == "__main__":
    print("--- Scraper Script: Fetching and Extracting Article Content ---")

    # List of MoEngage documentation URLs to scrape
    urls_to_scrape = [
        "https://partners.moengage.com/hc/en-us/articles/9643917325460-Create-creatives",
        "https://help.moengage.com/hc/en-us/articles/28194279371668-How-to-Analyze-OTT-Content-Performance",
        # Add more URLs here as needed for broader testing
    ]

    extracted_articles_data = []

    for url in urls_to_scrape:
        print(f"\nFetching content from: {url}")
        content = fetch_article_content(url)
        if content:
            print(f"Successfully extracted content (first 200 chars): \n{content[:200]}...")
            extracted_articles_data.append({"url": url, "content": content})
        else:
            print(f"Failed to extract content for: {url}")
            extracted_articles_data.append({"url": url, "content": None, "error": "Content extraction failed"})

    # Save the extracted data to a JSON file
    output_filename = "extracted_articles_complete.json"
    with open(output_filename, 'w', encoding='utf-8') as f:
        json.dump(extracted_articles_data, f, indent=4, ensure_ascii=False)

    print(f"\n--- Extraction complete. Data saved to {output_filename} ---")# moengage-doc-analysis/scraper.py

import requests
from bs4 import BeautifulSoup
import json
import os
from dotenv import load_dotenv

# Load environment variables (e.g., for API keys, though not strictly needed for scraping)
load_dotenv()

def fetch_article_content(url: str) -> str:
    """
    Fetches and parses the main content from a given URL.
    This function tries to extract the most relevant text content.
    """
    try:
        response = requests.get(url, timeout=10) # Added timeout for robustness
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Prioritize finding common article content tags
        # Adjust these selectors based on actual MoEngage documentation HTML structure
        article_content = soup.find('article') or \
                          soup.find('main') or \
                          soup.find('div', class_='article-body') or \
                          soup.find('div', id='main-content') # Common ZenDesk help center ID

        if article_content:
            # Remove script and style tags to clean the content
            for script_or_style in article_content(['script', 'style', 'nav', 'footer', 'header', 'aside']):
                script_or_style.extract()
            # Get text, strip whitespace, and replace multiple newlines with single ones
            text = article_content.get_text(separator='\n', strip=True)
            return "\n".join(filter(None, text.splitlines())) # Remove empty lines
        else:
            print(f"Warning: No specific article content tag found for {url}. Extracting body text.")
            # Fallback to body text if article-specific content is not found, but try to clean
            for script_or_style in soup.body(['script', 'style', 'nav', 'footer', 'header', 'aside']):
                script_or_style.extract()
            text = soup.body.get_text(separator='\n', strip=True)
            return "\n".join(filter(None, text.splitlines()))

    except requests.exceptions.Timeout:
        print(f"Error fetching URL {url}: Request timed out.")
        return ""
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return ""
    except Exception as e:
        print(f"Error parsing content from {url}: {e}")
        return ""

if __name__ == "__main__":
    print("--- Scraper Script: Fetching and Extracting Article Content ---")

    # List of MoEngage documentation URLs to scrape
    urls_to_scrape = [
        "https://partners.moengage.com/hc/en-us/articles/9643917325460-Create-creatives",
        "https://help.moengage.com/hc/en-us/articles/28194279371668-How-to-Analyze-OTT-Content-Performance",
        # Add more URLs here as needed for broader testing
    ]

    extracted_articles_data = []

    for url in urls_to_scrape:
        print(f"\nFetching content from: {url}")
        content = fetch_article_content(url)
        if content:
            print(f"Successfully extracted content (first 200 chars): \n{content[:200]}...")
            extracted_articles_data.append({"url": url, "content": content})
        else:
            print(f"Failed to extract content for: {url}")
            extracted_articles_data.append({"url": url, "content": None, "error": "Content extraction failed"})

    # Save the extracted data to a JSON file
    output_filename = "extracted_articles_complete.json"
    with open(output_filename, 'w', encoding='utf-8') as f:
        json.dump(extracted_articles_data, f, indent=4, ensure_ascii=False)

    print(f"\n--- Extraction complete. Data saved to {output_filename} ---")
    # moengage-doc-analysis/scraper.py

import requests
from bs4 import BeautifulSoup
import json
import os
from dotenv import load_dotenv

# Load environment variables (e.g., for API keys, though not strictly needed for scraping)
load_dotenv()

def fetch_article_content(url: str) -> str:
    """
    Fetches and parses the main content from a given URL.
    This function tries to extract the most relevant text content.
    """
    try:
        response = requests.get(url, timeout=10) # Added timeout for robustness
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Prioritize finding common article content tags
        # Adjust these selectors based on actual MoEngage documentation HTML structure
        article_content = soup.find('article') or \
                          soup.find('main') or \
                          soup.find('div', class_='article-body') or \
                          soup.find('div', id='main-content') # Common ZenDesk help center ID

        if article_content:
            # Remove script and style tags to clean the content
            for script_or_style in article_content(['script', 'style', 'nav', 'footer', 'header', 'aside']):
                script_or_style.extract()
            # Get text, strip whitespace, and replace multiple newlines with single ones
            text = article_content.get_text(separator='\n', strip=True)
            return "\n".join(filter(None, text.splitlines())) # Remove empty lines
        else:
            print(f"Warning: No specific article content tag found for {url}. Extracting body text.")
            # Fallback to body text if article-specific content is not found, but try to clean
            for script_or_style in soup.body(['script', 'style', 'nav', 'footer', 'header', 'aside']):
                script_or_style.extract()
            text = soup.body.get_text(separator='\n', strip=True)
            return "\n".join(filter(None, text.splitlines()))

    except requests.exceptions.Timeout:
        print(f"Error fetching URL {url}: Request timed out.")
        return ""
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return ""
    except Exception as e:
        print(f"Error parsing content from {url}: {e}")
        return ""

if __name__ == "__main__":
    print("--- Scraper Script: Fetching and Extracting Article Content ---")

    # List of MoEngage documentation URLs to scrape
    urls_to_scrape = [
        "https://partners.moengage.com/hc/en-us/articles/9643917325460-Create-creatives",
        "https://help.moengage.com/hc/en-us/articles/28194279371668-How-to-Analyze-OTT-Content-Performance",
        # Add more URLs here as needed for broader testing
    ]

    extracted_articles_data = []

    for url in urls_to_scrape:
        print(f"\nFetching content from: {url}")
        content = fetch_article_content(url)
        if content:
            print(f"Successfully extracted content (first 200 chars): \n{content[:200]}...")
            extracted_articles_data.append({"url": url, "content": content})
        else:
            print(f"Failed to extract content for: {url}")
            extracted_articles_data.append({"url": url, "content": None, "error": "Content extraction failed"})

    # Save the extracted data to a JSON file
    output_filename = "extracted_articles_complete.json"
    with open(output_filename, 'w', encoding='utf-8') as f:
        json.dump(extracted_articles_data, f, indent=4, ensure_ascii=False)

    print(f"\n--- Extraction complete. Data saved to {output_filename} ---")