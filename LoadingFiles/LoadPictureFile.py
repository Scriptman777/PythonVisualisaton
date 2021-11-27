import PIL
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

fig, axs = plt.subplots(2,2,figsize =(8, 8))

# Load image
img = PIL.Image.open('FIM.png')
# Convert to greyscale
img_g = img.convert('L')

# Create NumPy array from colored image
array_rgb = np.array(img)
# Create NumPy array from greyscale image
array_g = np.array(img_g)


axs[0][0].imshow(img)
axs[0][0].set_title("Pillow Image")

# Resize image
resized = img.resize((64, 64))

axs[0][1].imshow(resized)
axs[0][1].set_title("Resized")

# Laplace filter on array
filtered = ndimage.laplace(array_g)

axs[1][0].imshow(filtered, cmap='gray')
axs[1][0].set_title("Laplace filter")

# Sobel filter on array
sobel = ndimage.sobel(array_g)

axs[1][1].imshow(sobel, cmap='gray')
axs[1][1].set_title("Sobel filter")

new_img = PIL.Image.fromarray(filtered)

plt.show()