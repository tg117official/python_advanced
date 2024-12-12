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

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            return f"Failed to fetch HTML content. Status code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

# Example usage
if __name__ == "__main__":
    url = "https://www.flipkart.com/search?q=air+conditioners&sid=j9e%2Cabm%2Cc54&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_12_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_12_na_na_na&as-pos=1&as-type=RECENT&suggestionId=air+conditioners%7CAir+Conditioners&requestId=8a94da9b-17be-45b3-9f54-bd8af4784169&as-backfill=on"
    html_content = fetch_html(url)
    print(html_content)