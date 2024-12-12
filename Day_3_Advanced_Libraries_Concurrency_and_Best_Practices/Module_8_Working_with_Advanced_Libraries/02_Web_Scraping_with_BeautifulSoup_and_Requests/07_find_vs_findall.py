import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    """
    Fetches and parses the HTML content of a given website URL.

    Parameters:
        url (str): The URL of the website to fetch.

    Returns:
        BeautifulSoup: The parsed HTML content as a BeautifulSoup object, or None if the request fails.
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return BeautifulSoup(response.text, 'html.parser')
        else:
            print(f"Failed to fetch HTML content. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    url = "https://www.amazon.in/"
    soup = fetch_html(url)

    if soup:
        # Basic examples for the find method
        print("1. Find the first paragraph tag:")
        print(soup.find('p'))

        print("2. Find the first link tag:")
        print(soup.find('a'))

        print("3. Find the first div with a specific class:")
        print(soup.find('div', attrs={'class': 'copilot-secure-display'}))  # Replace with an actual class name on the page

        print("4. Find the first span with a specific ID:")
        print(soup.find('span', id='nav-link-accountList-nav-line-1'))  # Replace with an actual ID

        print("5. Find the first input tag:")
        print(soup.find('input'))

        print("6. Find the first script tag:")
        print(soup.find('script'))

        print("7. Find the first link tag with rel='stylesheet':")
        print(soup.find('link', rel='stylesheet'))

        print("8. Find the first image tag:")
        print(soup.find('img'))

        print("9. Find the first header tag (h1):")
        print(soup.find('h1'))

        print("10. Find the first meta tag with a name attribute:")
        print(soup.find('meta', attrs={'name': 'description'}))  # Replace 'description' with an actual name if available

        # Examples for the find_all method
        print("\nExamples for the find_all method:")

        print("1. Find all paragraph tags:")
        for p in soup.find_all('p', limit=5):
            print(p)

        print("2. Find all link tags:")
        for a in soup.find_all('a', limit=5):
            print(a.get('href'))

        print("3. Find all div tags:")
        for div in soup.find_all('div', limit=5):
            print(div)

        print("4. Find all images with source attributes:")
        for img in soup.find_all('img', limit=5):
            print(img.get('src'))

        print("5. Find all script tags with source attributes:")
        for script in soup.find_all('script', limit=5):
            print(script.get('src'))

        print("6. Find all meta tags with name attribute:")
        for meta in soup.find_all('meta', attrs={'name': True}, limit=5):
            print(meta)

        print("7. Find all headers (h1, h2, h3):")
        for header in soup.find_all(['h1', 'h2', 'h3'], limit=5):
            print(header)

        print("8. Find all links with specific class:")
        for link in soup.find_all('a', class_='nav-a', limit=5):  # Replace 'nav-a' with a relevant class
            print(link)

        print("9. Find all spans with specific attributes:")
        for span in soup.find_all('span', attrs={'class': 'nav-text'}, limit=5):  # Replace 'nav-text' with a relevant class
            print(span)

        print("10. Find all input fields:")
        for input_tag in soup.find_all('input', limit=5):
            print(input_tag)
