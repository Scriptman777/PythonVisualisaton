from urllib.request import urlopen
from bs4 import BeautifulSoup
import wordcloud
import matplotlib.pyplot as plt
import numpy as np
import PIL

text = open("FIM.txt", encoding="utf8").read()
mask = np.array(PIL.Image.open("FIM4.png"))

skip_words = ["v", "je", "na", "k", "i", "ve", "o", "s", "z", "ke", "a", "se", "si", "ze", "za", "do", "od", "po", "pro","při"]


cloud = wordcloud.WordCloud(stopwords=skip_words, background_color="white", mask=mask, width=2000, height=1000, collocations=False).generate(text)
image_colors = wordcloud.ImageColorGenerator(mask)


plt.figure(figsize=(20,10), facecolor='k')
plt.imshow(cloud.recolor(color_func=image_colors),interpolation="bilinear")
plt.axis("off")
plt.show()