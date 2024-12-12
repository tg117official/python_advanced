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

        print("3. Meta Tags:")
        for meta in soup.find_all('meta'):
            print(meta)

        print("4. First Link:", soup.find('a'))  # Prints the first <a> tag

        print("5. All Links:")
        for link in soup.find_all('a', limit=5):  # Prints the first 5 <a> tags
            print(link.get('href'))

        print("6. First Div Tag:", soup.find('div'))  # Prints the first <div> tag

        print("7. All Div Tags:")
        for div in soup.find_all('div', limit=5):  # Prints the first 5 <div> tags
            print(div)

        print("8. First Image Tag:", soup.find('img'))  # Prints the first <img> tag

        print("9. All Image Sources:")
        for img in soup.find_all('img', limit=5):  # Prints the first 5 image sources
            print(img.get('src'))

        print("10. All Headers (h1, h2, h3):")
        for header in soup.find_all(['h1', 'h2', 'h3'], limit=5):  # Prints the first 5 header tags
            print(header.text)

        print("11. Footer Section:", soup.find('footer'))  # Prints the <footer> tag if present

        print("12. Search for a specific class:")
        element = soup.find(class_="navFooterDescText")  # Replace with an actual class
        print(element)

        print("13. Extracting all CSS Links:")
        for css in soup.find_all('link', {'rel': 'stylesheet'}):
            print(css.get('href'))

        print("14. Extracting all JavaScript Files:")
        for script in soup.find_all('script'):
            print(script.get('src'))

        print("15. Paragraphs in the Page:")
        for paragraph in soup.find_all('p', limit=5):  # Prints the first 5 paragraphs
            print(paragraph.text)
