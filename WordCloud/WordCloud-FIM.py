from urllib.request import urlopen
from bs4 import BeautifulSoup
import wordcloud
import matplotlib.pyplot as plt
import numpy as np
import PIL

text = open("FIM.txt").read()
mask = np.array(PIL.Image.open("FIM4.png"))

cloud = wordcloud.WordCloud(background_color="white", mask=mask, width=2000, height=1000).generate(text)
image_colors = wordcloud.ImageColorGenerator(mask)


plt.figure(figsize=(20,10), facecolor='k')
plt.imshow(cloud.recolor(color_func=image_colors),interpolation="bilinear")
plt.axis("off")
plt.show()