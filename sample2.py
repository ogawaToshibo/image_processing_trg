import cv2, matplotlib
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('images/1.JPG')
# print(img)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# plt.imshow(img)
# plt.imshow(img)
# plt.show()

gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# print(gray_img)
# plt.imshow(gray_img)
# plt.show()

average_color_per_row = np.average(img, axis=0)

average_color = np.average(average_color_per_row, axis=0)

average_color = np.uint8(average_color)
# print(average_color)

average_color_img = np.array([[average_color]*100]*100, np.uint8)

# plt.imshow(average_color_img)
# plt.show()

_, threshold_img = cv2.threshold(gray_img, 60, 255, cv2.THRESH_BINARY)

threshold_img = cv2.cvtColor(threshold_img, cv2.COLOR_GRAY2RGB)
plt.imshow(threshold_img)
plt.show()