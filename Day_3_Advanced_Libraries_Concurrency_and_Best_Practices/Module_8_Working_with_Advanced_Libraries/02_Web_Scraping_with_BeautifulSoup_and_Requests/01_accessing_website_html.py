import requests

def fetch_html(url):
    """
    Fetches the HTML content of a given website URL.

    Parameters:
        url (str): The URL of the website to fetch.

    Returns:
        str: The HTML content of the website, or an error message if the request fails.
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return f"Failed to fetch HTML content. Status code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

# Example usage
if __name__ == "__main__":
    url = "https://www.amazon.in/"
    html_content = fetch_html(url)
    print(html_content)