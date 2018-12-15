import cv2
import numpy as np
from collections import deque
import pytesseract

img = cv2.imread('IMG_1833.jpg')
cv2.imshow("org",img)
denoised = cv2.medianBlur(img,7)

gray_img = cv2.cvtColor(denoised,cv2.COLOR_BGR2GRAY)
# gaussianadaptivethresimg = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
#                                                  cv2.THRESH_BINARY_INV, 11, 2)
# #
# cv2.imshow("bef",gaussianadaptivethresimg)
# gaussianadaptivethresimg = cv2.erode(gaussianadaptivethresimg,(3,1),iterations=3)
# img = cv2.dilate(gaussianadaptivethresimg,(5,5),iterations=5)
# img = cv2.resize(gaussianadaptivethresimg,(0,0),fx=0.5,fy=0.5)
cv2.imshow("af",img)

result = pytesseract.image_to_string(gray_img, lang="sin")
print (result)

cv2.waitKey(0)