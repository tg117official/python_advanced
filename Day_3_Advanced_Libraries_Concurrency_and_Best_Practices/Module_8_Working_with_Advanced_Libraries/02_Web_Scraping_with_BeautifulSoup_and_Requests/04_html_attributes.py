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
        # Basic examples for accessing tags and content
        print("1. Title Tag:", soup.title)  # Prints the <title> tag
        print("2. Title Text:", soup.title.string)  # Prints the text inside the <title> tag

        print("3. Meta Tags and Attributes:")
        for meta in soup.find_all('meta'):
            print(meta, "Attributes:", meta.attrs)

        print("4. First Link and Attributes:")
        first_link = soup.find('a')
        print(first_link, "Attributes:", first_link.attrs)

        print("5. All Links with Attributes:")
        for link in soup.find_all('a', limit=5):
            print(link.get('href'), "Attributes:", link.attrs)

        print("6. First Image Tag and Attributes:")
        first_img = soup.find('img')
        print(first_img, "Attributes:", first_img.attrs)

        print("7. All Images with Attributes:")
        for img in soup.find_all('img', limit=5):
            print(img.get('src'), "Attributes:", img.attrs)

        print("8. Script Tags and Attributes:")
        for script in soup.find_all('script', limit=5):
            print(script.get('src'), "Attributes:", script.attrs)

        print("9. Links to Stylesheets with Attributes:")
        for css in soup.find_all('link', {'rel': 'stylesheet'}):
            print(css.get('href'), "Attributes:", css.attrs)

        print("10. Divs with Specific Attributes:")
        for div in soup.find_all('div', limit=5):
            print(div, "Attributes:", div.attrs)
