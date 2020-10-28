import cv2
import numpy as np
img = cv2.imread('shapes.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

conf_map = cv2.cornerHarris(src=gray, blockSize=3, ksize=3, k=0.04)

res = np.copy(img)
threshold = 0.01*conf_map.max()
res[conf_map> threshold] = [255,0,0] #c가 임계값보다 크면 coner, blue
res[conf_map<= threshold] = [0,0,255] #c가 0에 가까우면 flat, red
res[conf_map< 0] = [255,255,255] #c가 음수이면 edge, 하얀색

concatenated = np.hstack((img, res))
concatenated = cv2.resize(concatenated, None, fx=2.0, fy=2.0)
cv2.imshow('harris corner', concatenated)
cv2.waitKey()

cv2.destroyAllWindows()