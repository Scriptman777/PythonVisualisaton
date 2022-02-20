from urllib.request import urlopen
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
import PIL
import random

# Recolor words to fit the color scheme of the city

def recolor_func(word, font_size, position, orientation, random_state=None, **kwargs):
    
    if (random.randint(0, 100) > 30):
        light = int(random.randint(30, 60))
        return "hsl({}, {}%, {}%)".format(29, 100, light)
    else:
        light = int(random.randint(60, 100))
        return "hsl({}, {}%, {}%)".format(0, 0, light)
    

# GET DATA

# Open a page from the website
url = "https://www.novemestonm.cz/o-meste/zakladni-informace/"
webpage = urlopen(url)
page_content = webpage.read().decode("utf-8")
soup = BeautifulSoup(page_content, "html.parser")

# Find all links to other parts of the site and create a list of URLs
link_list = soup.find_all("a")
urls = []
for link in link_list:
    if not str(link.get("class")).rfind("nav-link") == -1:
        urls.append(link.get("href"))
    
all_text = ""
progress = 0

# Get all text from found pages
for subpage in urls:

    try:
        webpage = urlopen("https://www.novemestonm.cz/" + subpage)
        progress += 1
        print("https://www.novemestonm.cz/" + subpage)
        print("Progress: [" + str(progress) + "/" + str(len(urls)) + "]")        
        page_content = webpage.read().decode("utf-8")
        soup = BeautifulSoup(page_content, "html.parser")
        # Select only the div that has page content, ignore the rest
        content_divs = soup.find_all("div", {"class": "editor_content readable"})
        for div in content_divs:
            all_text = all_text + div.text
    except:
        pass


# VISUALIZE DATA

# Load a silhouette of the chateau as an array to apply to the word cloud
mask = np.array(PIL.Image.open("NMNM.png"))
# Skip common words that have no meaning by themselves
skip_words = ["v", "je", "na", "k", "i", "ve", "o", "s", "z", "ke", "a", "se", "si", "ze", "za", "do", "od", "po", "pro","při", "cz", "www", "e"]

# Create a Wordcloud with created mask
cloud = WordCloud(stopwords=skip_words, max_words=1000, collocations=False, background_color="black", mask=mask, contour_width=3, contour_color='white').generate(all_text)
# Use defined recolor function
cloud.recolor(color_func=recolor_func)
# Save to file
cloud.to_file('WordCloudNMNM.png')
# Use Matplotlib to show file in a window
plt.figure(figsize=(10,7.5))
plt.imshow(cloud, interpolation="bilinear")
plt.axis("off")
plt.show()