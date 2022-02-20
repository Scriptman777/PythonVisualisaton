from urllib.request import urlopen
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import numpy as np
import PIL
import random

# Define a function to recolor text to shades of red

def recolor_func(word, font_size, position, orientation, random_state=None, **kwargs):
        light = int(random.randint(30, 60))
        return "hsl({}, {}%, {}%)".format(0, 100, light)

    
# GET DATA

# Get text from wikipedia page
url = "https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC"
webpage = urlopen(url)
page_content = webpage.read().decode("utf-8")
soup = BeautifulSoup(page_content, "html.parser")
text = soup.get_text()

# Load font that contains japanese characters
font = "NotoSansCJKjp-Light.otf"

# Load flag to use as mask
mask = np.array(PIL.Image.open("flag2.png"))

# VISUALIZE DATA

cloud = WordCloud(max_words=1000, background_color="white", font_path=font, collocations=False, mask=mask).generate(soup.get_text())
cloud.recolor(color_func=recolor_func)
image = cloud.to_image()
image.show()