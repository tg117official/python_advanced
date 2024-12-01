import requests
from bs4 import BeautifulSoup

# Exercise 1: Fetch and parse a web page
# Problem: Fetch the HTML content of a web page and parse it using BeautifulSoup.
# Relevance: Core skill in web scraping, used to analyze and process web data.
url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
print("Exercise 1 Result:", soup.title.string)  # Output: Example Domain

# Exercise 2: Extract all links from a web page
# Problem: Write a script to extract all hyperlinks (`<a>` tags) from a web page.
# Relevance: Commonly used for crawling and indexing web pages.
url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
links = [a["href"] for a in soup.find_all("a", href=True)]
print("\nExercise 2 Result:", links)  # Output: ['/']

# Exercise 3: Extract text from a specific HTML element
# Problem: Extract the main heading (`<h1>` tag) from a web page.
# Relevance: Useful for extracting structured data, such as headlines or titles.
url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
heading = soup.find("h1").get_text()
print("\nExercise 3 Result:", heading)  # Output: Example Domain

# Exercise 4: Find all images on a web page
# Problem: Extract all image URLs (`<img>` tags) from a web page.
# Relevance: Used in image analysis, download automation, or building datasets.
url = "https://www.wikipedia.org/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
images = [img["src"] for img in soup.find_all("img", src=True)]
print("\nExercise 4 Result:", images[:5])  # Output: First 5 image URLs

# Exercise 5: Extract data from a table
# Problem: Write a script to scrape and extract data from an HTML table.
# Relevance: Frequently used to scrape tabular data like stock prices, statistics, etc.
url = "https://www.w3schools.com/html/html_tables.asp"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
table = soup.find("table", {"id": "customers"})
rows = table.find_all("tr")
table_data = []
for row in rows:
    cells = [cell.get_text(strip=True) for cell in row.find_all(["th", "td"])]
    table_data.append(cells)
print("\nExercise 5 Result:", table_data[:3])  # Output: First 3 rows of the table
