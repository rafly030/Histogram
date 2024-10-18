import imageio
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Read the RGB image
rgb_image = imageio.imread('spongebob.png')

# Step 2: Convert the image to grayscale
grayscale_image = 0.2989 * rgb_image[:, :, 0] + 0.5870 * rgb_image[:, :, 1] + 0.1140 * rgb_image[:, :, 2]

# Step 3: Calculate the histogram of the grayscale image
histogram, bin_edges = np.histogram(grayscale_image, bins=256, range=(0, 255))

# Step 4: Plot the histogram
plt.plot(bin_edges[0:-1], histogram)
plt.xlim([0, 255])
plt.title('Histogram of Grayscale Image')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.show()