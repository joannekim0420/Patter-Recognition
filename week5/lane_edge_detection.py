import cv2

""" #picture
img = cv2.imread('solidWhiteRight.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred_img = cv2.GaussianBlur(gray_img, (3,3), 0.0)
# cv2.imshow('blurred', blurred_img)
# cv2.waitKey()

edge_img = cv2.Canny(blurred_img, 70, 140)
cv2.imshow('edge', edge_img)
cv2.waitKey()
"""

#video
def pipeline(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred_img = cv2.GaussianBlur(gray_img, (3, 3), 0.0)
    edge_img = cv2.Canny(blurred_img, 70, 140)
    return edge_img

cap = cv2.VideoCapture('./test_videos/solidWhiteRight.mp4')
while True:
    ok, frame = cap.read()
    if not ok:
        break

    edge_img= pipeline(frame)
    cv2.imshow('frame', edge_img)
    #1000 = 1초
    key = cv2.waitKey(30)

    if key== ord('x'):
        break   #x를 누르면 빠져 나옴

cap.release() #비디오 파일을 잡고 있기 때문에 마지막엔 release 해줘야함.