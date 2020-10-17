import cv2
import matplotlib.pyplot as plt

img = cv2.imread('LondonEye.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow('image', gray_img)

plt.hist(gray_img.ravel(),256,[0,256])
plt.show()



