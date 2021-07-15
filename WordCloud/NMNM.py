from urllib.request import urlopen
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
import PIL
import random



url = "https://www.novemestonm.cz/o-meste/zakladni-informace/"
webpage = urlopen(url)
page_content = webpage.read().decode("utf-8")
soup = BeautifulSoup(page_content, "html.parser")

link_list = soup.find_all("a")
urls = []
for link in link_list:
    if not str(link.get("class")).rfind("nav-link") == -1:
        urls.append(link.get("href"))
    
all_text = ""
progress = 0

for subpage in urls:

    try:
        webpage = urlopen("https://www.novemestonm.cz/" + subpage)
        progress += 1
        print("https://www.novemestonm.cz/" + subpage)
        print("Progress: [" + str(progress) + "/" + str(len(urls)) + "]")        
        page_content = webpage.read().decode("utf-8")
        soup = BeautifulSoup(page_content, "html.parser")
        content_divs = soup.find_all("div", {"class": "editor_content readable"})
        for div in content_divs:
            all_text = all_text + div.text
    except:
        pass
    
mask = np.array(PIL.Image.open("NMNM.png"))

cloud = WordCloud(max_words=1000, background_color="white", width=2000, height=1000, mask=mask, contour_width=3, contour_color='black').generate(all_text)


plt.figure(figsize=(20,10))
plt.imshow(cloud, interpolation="bilinear")
plt.axis("off")
plt.show()