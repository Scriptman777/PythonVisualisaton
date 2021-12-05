from bs4 import BeautifulSoup
from urllib.request import urlopen


# Load article from https://www.uhk.cz/cs/univerzita-hradec-kralove/uhk/o-univerzite

# Open url
page_url = urlopen("https://www.uhk.cz/cs/univerzita-hradec-kralove/uhk/o-univerzite")
# Read whole page
all_content = page_url.read().decode("utf-8")
# Create a BeautifulSoup object
soup = BeautifulSoup(all_content, "html.parser")
# Text of article is in class "wysiwyg-content", there can be more results
results = soup.find_all(class_="wysiwyg-content")
# Get text from div(s)
content_list = []
for result in results:
    content_list.append(result.get_text())


print(content_list)