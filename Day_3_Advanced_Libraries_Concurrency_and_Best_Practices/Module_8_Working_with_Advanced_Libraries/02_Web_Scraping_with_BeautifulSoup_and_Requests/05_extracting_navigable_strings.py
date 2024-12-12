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
        # Basic examples for accessing navigable strings
        print("1. Title Text:", soup.title.string)  # Extracts the navigable string inside the <title> tag

        print("2. First Paragraph Text:")
        first_paragraph = soup.find('p')
        if first_paragraph:
            print(first_paragraph.string)

        print("3. All Paragraph Texts:")
        for paragraph in soup.find_all('p', limit=5):
            print(paragraph.string)

        print("4. First Link Text:")
        first_link = soup.find('a')
        if first_link:
            print(first_link.string)

        print("5. All Link Texts:")
        for link in soup.find_all('a', limit=5):
            print(link.string)

        print("6. First Header Text (h1):")
        first_header = soup.find('h1')
        if first_header:
            print(first_header.string)

        print("7. All Header Texts (h1, h2, h3):")
        for header in soup.find_all(['h1', 'h2', 'h3'], limit=5):
            print(header.string)

        print("8. Div Texts:")
        for div in soup.find_all('div', limit=5):
            if div.string:
                print(div.string)

        print("9. Span Texts:")
        for span in soup.find_all('span', limit=5):
            if span.string:
                print(span.string)

        print("10. Navigable String from Custom Tag:")
        custom_tag = soup.find('footer')  # Example with footer, can be changed
        if custom_tag and custom_tag.string:
            print(custom_tag.string)
