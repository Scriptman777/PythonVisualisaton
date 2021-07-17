from urllib.request import urlopen
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import numpy as np
import PIL
import random

def recolor_func(word, font_size, position, orientation, random_state=None, **kwargs):
        light = int(random.randint(30, 60))
        return "hsl({}, {}%, {}%)".format(0, 100, light)

    


url = "https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC"
webpage = urlopen(url)
page_content = webpage.read().decode("utf-8")
soup = BeautifulSoup(page_content, "html.parser")
text = soup.get_text()
    
font = "NotoSansCJKjp-Light.otf"

mask = np.array(PIL.Image.open("flag2.png"))


cloud = WordCloud(max_words=1000, background_color="white", font_path=font, collocations=False, mask=mask).generate(soup.get_text())
cloud.recolor(color_func=recolor_func)
image = cloud.to_image()
image.show()