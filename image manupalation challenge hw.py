#the cw code part 2(only brightness part), typed as hw

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('images.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


# Increase brightness by adding 50 to all pixel values
# Use cv2.add to avoid negative values or overflow
brightness_matrix = np.ones(image.shape, dtype="uint8") * 50
brighter = cv2.add(image, brightness_matrix)

brighter_rgb = cv2.cvtColor(brighter, cv2.COLOR_BGR2RGB)
plt.imshow(brighter_rgb)
plt.title("Brighter Image")
plt.show()