import cv2
import matplotlib.pyplot as plt

img = cv2.imread('lenna.png')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow('image', gray_img)

plt.hist(gray_img.ravel(),256,[0,256])
plt.show()


#cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
#images = 분석할 이미지 list
#channels = BGR (1-channel이면 [0], 3-channel [0,2])
#mask = 분석할 이미지 영역 마스크, none=전체영역
#histSize - bin의 개수[256]
#ranges - 히스토그램의 분석 범위 [0,256]

#답
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# hist = cv2.calcHist(gray, [0], None, [256],[0,256])
# plt.plot(hist)
# plt.show()
