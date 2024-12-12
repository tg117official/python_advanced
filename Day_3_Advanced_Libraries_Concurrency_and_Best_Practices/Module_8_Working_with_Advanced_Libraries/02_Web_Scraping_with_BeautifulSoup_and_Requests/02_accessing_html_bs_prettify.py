import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    """
    Fetches and parses the HTML content of a given website URL.

    Parameters:
        url (str): The URL of the website to fetch.

    Returns:
        str: The parsed HTML content of the website, or an error message if the request fails.
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup.prettify()
        else:
            return f"Failed to fetch HTML content. Status code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

# Example usage
if __name__ == "__main__":
#    url = "https://www.amazon.in/"
    url = "https://www.amazon.in/hz/mobile/mission?p=s3rLV1%2FLkbf%2FKbsb8K7ZnKlJUPsXQsjeapOPFa552hcVKGl%2F6nD7p1C%2B58iysnuugeXpgsyJH0HC8%2BCRMTRRFjifnUnzZNSHbCq9UfLgnONqEYJcV2xwR1R8XaChO%2BJih4nsExouln87dwxr%2Bo1pDZgezSoBEiePTj7skohzhR%2Bhf%2B7dteHAEYws4younzUUWoHYOXXx47q9D%2BPPlG2XQlrIn0WJQCB4KQB4l57AMpRv9IDEyOI1b%2BPHDPsTryi%2BxVdr1qzqcXLb5hYSX%2B%2F1MV4d4XmCjwrdBqcJFhggEO3SYCZFXRNvcQ69R%2FYsaqEu3LvvFyQfloBqrhPNyRE4zgCPWkrnMQvhTs%2FzUKVhVggw%2BW1rB616q8ssSRAbtqsRXCcC1GIh5fCUrK7jTYKNAClaQVwasgFJiB%2BWqz3econmxqDhpd6%2BWw%3D%3D&ref_=nb_sb_ss_di_ci_mcx_mi_ci-mcx-ksf-of-nv1_0&crid=66Y858WZBWMY"
    html_content = fetch_html(url)
    print(html_content)
