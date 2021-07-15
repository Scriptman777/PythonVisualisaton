from urllib.request import urlopen
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import PIL

url = "https://www.uhk.cz/cs/univerzita-hradec-kralove/uhk/o-univerzite"
webpage = urlopen(url)
page_content = webpage.read().decode("utf-8")
soup = BeautifulSoup(page_content, "html.parser")

link_list = soup.find_all("a")
urls = []
for link in link_list:
    if not str(link.get("href")).rfind("/cs/") == -1:
        urls.append(link.get("href"))
    
all_text = ""

for subpage in urls:
    try:
        webpage = urlopen("https://www.uhk.cz" + subpage)
        print("https://www.uhk.cz" + subpage)
        page_content = webpage.read().decode("utf-8")
        soup = BeautifulSoup(page_content, "html.parser")
        all_text = all_text + soup.get_text()
    except :
        pass
    


cloud = WordCloud(max_words=1000, background_color="white", width=2000, height=1000).generate(all_text)

image = cloud.to_image()
image.show()