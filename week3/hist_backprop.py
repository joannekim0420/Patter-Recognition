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

# #normalization
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
hist_r = hist_m / (hist_i+1e-7)
hist_r = np.minimum(hist_r, 1)
print("range of hist_r: [%.1f, %.1f]" %(hist_r.min(), hist_r.max()))

#backprojection
h,s,v = cv2.split(hsv_i)
result = hist_r[h, s] #my code

#
# height, width = img_i.shape[0], img_i.shape[1]
# result = np.zeros_like(img_i, dtype='float32')
# h,s,v = cv2.split(hsv_i)

# for i in range(height):
#     for j in range(width):
#         h_value = h[i,j]
#         s_value = s[i,j]
#         confidence = hist_r[h_value, s_value]
#         result[i, j] = confidence

#binarization
ret, thresholded = cv2.threshold(result, 0.002, 255, cv2.THRESH_BINARY)
cv2.imwrite('result_202009.jpg', thresholded)

#morphology

img = cv2.imread('result_202009.jpg',0)
kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(img,kernel,iterations = 1)
dilation = cv2.dilate(dilation,kernel,iterations = 1)
dilation = cv2.dilate(dilation,kernel,iterations = 1)
dilation = cv2.dilate(dilation,kernel,iterations = 1)
cv2.imwrite('morphology_3.jpg', dilation)
erosion = cv2.erode(dilation,kernel,iterations = 1)
erosion = cv2.erode(erosion,kernel,iterations = 1)
erosion = cv2.erode(erosion,kernel,iterations = 1)
cv2.imwrite('morphology_4.jpg', erosion)