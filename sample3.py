import cv2, matplotlib
import numpy as np
import matplotlib.pyplot as plt

blue_min = np.array([100, 100, 100], np.uint8)
blue_max = np.array([140, 255, 255], np.uint8)

upstate = cv2.imread('images/2.JPG')
upstate_hsv = cv2.cvtColor(upstate, cv2.COLOR_BGR2HSV)
plt.imshow(cv2.cvtColor(upstate_hsv, cv2.COLOR_HSV2RGB))

mask_inverse = cv2.inRange(upstate_hsv, blue_min, blue_max)

mask = cv2.bitwise_not(mask_inverse)
plt.imshow(cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB))

mask_rgb = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)

masked_upstate = cv2.bitwise_and(upstate, mask_rgb)

masked_replace_white = cv2.addWeighted(masked_upstate, 1, cv2.cvtColor(mask_inverse, cv2.COLOR_GRAY2RGB), 1, 0)

plt.imshow(cv2.cvtColor(masked_replace_white, cv2.COLOR_BGR2RGB))
plt.show()