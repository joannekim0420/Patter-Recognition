import cv2
import timeit
import time
#import util

filepath = 'eifleTower.jpg'
img = cv2.imread(filepath)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

h, w = img.shape[0:2]
print(w,h)

#sift
sift_start= timeit.default_timer()
sift = cv2.xfeatures2d.SIFT_create()
sift_kpts = sift.detect(image=gray, mask=None)
sift_res = cv2.drawKeypoints(image=gray, keypoints=sift_kpts, outImage=None)
sift_end = timeit.default_timer()
print(f"SIFT Runtime: {sift_end - sift_start}")

#surf
surf_start= time.time()
surf = cv2.xfeatures2d.SURF_create()
surf_kpts = surf.detect(image=gray, mask=None)
surf_res = cv2.drawKeypoints(image=gray, keypoints=surf_kpts, outImage=None)
surf_end = time.time()
print(f"SURF Runtime: {surf_end - surf_start}")


############## RESULT #################
## 3024 4032                         ##
## SIFT Runtime: 3.0787005           ##
## SURF Runtime: 2.9132163524627686  ##
#######################################


# sift_res_with_rich = cv2.drawKeypoints(image=gray, keypoints=sift_kpts, outImage=None, flags=4)
# sift_concatenated = np.hstack((sift_res, sift_res_with_rich))
# cv2.imshow('concatenated', sift_concatenated)
# cv2.waitKey(0)

