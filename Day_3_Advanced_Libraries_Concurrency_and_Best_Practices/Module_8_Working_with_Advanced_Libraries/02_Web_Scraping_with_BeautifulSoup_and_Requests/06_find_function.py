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
        print(soup.find('span', attrs={'id':'nav-menu-label', 'class':'nav-hidden-aria'}))  # Replace with an actual ID

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
