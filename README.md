# Patter-Recognition

- matplotlib 
  R,G,B순서\
  cv2.imshow() : uint8 [0,255], float32 [0.0, 1.0]
  
- opencv 
  B,G,R순서\
  plt.imshow() [0,255] 정규화한 결과 출력
  
- img.shape : (height, width, n_channel)


### cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
images = 분석할 이미지 list\
channels = BGR (1-channel이면 [0], 3-channel [0,2])\
mask = 분석할 이미지 영역 마스크, none=전체영역\
histSize - bin의 개수[256]\
ranges - 히스토그램의 분석 범위 [0,256]\

kernel = np.ones((5,5),np.uint8)
### dilation = cv2.dilate(img,kernel,iterations = 3)
팽창 연산\
iterations = 연산을 반복할 횟수

### erosion = cv2.erode(dilation,kernel,iterations = 3)
침식 연산\
iterations = 연산을 반복할 횟수

### cv2.morphologyEx(img, cv2.MORTH_CLOSE, kernel)
cv2.MORTH_CLOSE, cv2.MORTH_OPEN

### cv_M = cv2.getRotationMatrix2D(center, 90, 1.0)
center = 회전의 기준이 되는 좌표\
counter clockwise 90도 만큼\
크기는 1배로 유지해서

### cv_result = cv2.warpAffine(img, cv_M, (width, height))
img = input image\
cv_result = output image\
cv_M = Affine transform, 적용할 매트릭스\
(width, height) = ouput 영상의 사이즈 

### blurred_img = cv2.GaussianBlur(gray_img, (3,3), 0.0)
(input_image, kernel_size, sigma)

### edge_img = cv2.Canny(blurred_img, 70, 140)
(input_image, low_th, high_th)
