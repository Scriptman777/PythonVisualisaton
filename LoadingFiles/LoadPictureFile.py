import PIL.Image
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

fig, axs = plt.subplots(2,2,figsize =(8, 8))


img = PIL.Image.open('FIM.png')
img_g = img.convert('L')
array = np.array(img_g)


axs[0][0].imshow(img)
axs[0][0].set_title("Pillow Image")


resized = img.resize((64, 64))

axs[0][1].imshow(resized)
axs[0][1].set_title("Resized")


filtered = ndimage.laplace(array)

axs[1][0].imshow(filtered, cmap='gray')
axs[1][0].set_title("Laplace filter")


sobel = ndimage.sobel(array)

axs[1][1].imshow(sobel, cmap='gray')
axs[1][1].set_title("Sobel filter")


plt.show()