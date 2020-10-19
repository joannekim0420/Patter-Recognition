import cv2
import numpy as np

#model_img
img_m = cv2.imread('model.jpg')
hsv_m = cv2.cvtColor(img_m, cv2.COLOR_BGR2HSV)
hist_m = cv2.calcHist([hsv_m],[0,1],None, [180,256],[0,180,0,256])

#input_img
img_i = cv2.imread('hand.jpg')
hsv_i = cv2.cvtColor(img_i, cv2.COLOR_BGR2HSV)
hist_i = cv2.calcHist([hsv_i],[0,1],None, [180,256],[0,180,0,256])

#normalization
#정규화 진행하지 않으면, 입력 이미지가 모델 이미지에 비해 너무 클 때,
#모델 이미지 입력 이미지의 크기 차이로 비율 히스토그램(모델 히스토그램/인풋 히스토그램)이 0에 수렴
pixels_m = img_m.shape[0] * img_m.shape[1]
pixels_i = img_i.shape[0] * img_i.shape[1]
#=pixels_m = img_i.size

hist_m = hist_m/(pixels_m)
hist_i = hist_i/(pixels_i)

# print("maximum of his_m: %f" %hist_m.max())
# print("maximum of his_m: %f" %hist_m.sum())
# print("maximum of his_i: %f" %hist_i.max())
# print("maximum of his_m: %f" %hist_i.sum())

# #r_hist
hist_r = hist_m / (hist_i+1e-7) #0으로 나눠지는 오류를 방지하기 위해 작은 값 더함.
hist_r = np.minimum(hist_r, 1)
print("range of hist_r: [%.1f, %.1f]" %(hist_r.min(), hist_r.max()))

#backprojection
h,s,v = cv2.split(hsv_i)
result = hist_r[h, s] #my code

#답
"""
height, width = img_i.shape[0], img_i.shape[1]
result = np.zeros_like(img_i, dtype='float32')
h,s,v = cv2.split(hsv_i)

for i in range(height):
    for j in range(width):
        h_value = h[i,j]
        s_value = s[i,j]
        confidence = hist_r[h_value, s_value]
        result[i, j] = confidence
"""

#binarization
ret, thresholded = cv2.threshold(result, 0.02, 255, cv2.THRESH_BINARY)
cv2.imwrite('result_20201019.jpg', thresholded)

#morphology
kernel = np.ones((5,5),np.uint8)
#my code
dilation = cv2.dilate(thresholded,kernel,iterations = 3)
cv2.imwrite('morphology_dilation.jpg', dilation)
erosion = cv2.erode(dilation,kernel,iterations = 3)
cv2.imwrite('morphology_erosion.jpg', erosion)

#답
"""
improved = cv2.morphologyEx(thresholded, cv2.MORTH_, kernel)
cv2.imwrite('morphology.jpg')
"""