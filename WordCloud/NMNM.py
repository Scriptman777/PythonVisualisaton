from urllib.request import urlopen
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
import PIL
import random

def recolor_func(word, font_size, position, orientation, random_state=None, **kwargs):
    
    if (random.randint(0, 100) > 30):
        light = int(random.randint(30, 60))
        return "hsl({}, {}%, {}%)".format(29, 100, light)
    else:
        light = int(random.randint(60, 100))
        return "hsl({}, {}%, {}%)".format(0, 0, light)
    


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
skip_words = ["v", "je", "na", "k", "i", "ve", "o", "s", "z", "ke", "a", "se", "si", "ze", "za", "do", "od", "po", "pro","při", "cz", "www", "e"]

cloud = WordCloud(stopwords = skip_words, max_words=1000, collocations=False, background_color="black", mask=mask, contour_width=3, contour_color='white').generate(all_text)
cloud.recolor(color_func=recolor_func)

cloud.to_file('WordCloudNMNM.png')

plt.figure(figsize=(10,7.5))
plt.imshow(cloud, interpolation="bilinear")
plt.axis("off")
plt.show()