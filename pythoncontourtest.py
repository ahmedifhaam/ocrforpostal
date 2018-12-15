import cv2
import numpy as np
import os


name = 'wasthi'

path = 'imgs/second/'+name+'.jpeg'
img = cv2.imread(path,-1)
orginal = img.copy()
img = cv2.medianBlur(img,7)
# denoised = cv2.medianBlur(img,7)
img2 = img.copy()
# img2 = denoised
# cv2.imshow("original.jpeg",img)

gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

# ret, threshed_img = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
threshed_img = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                          cv2.THRESH_BINARY_INV, 11, 2)
# cv2.imshow("threshed",threshed_img)

threshed_img = cv2.dilate(threshed_img,(25,1),iterations=10)

# cv2.imshow("dilated",threshed_img)
image,contours,hier = cv2.findContours(threshed_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

#
# black = np.zeros_like(img)
# cv2.imshow("black.jpg",black)

contours = sorted(contours,key=lambda ctr:cv2.boundingRect(ctr)[0])

print(contours.__sizeof__().__str__() + "Size")
index = 0

# print(hier)

rects = []

for cnt in contours:
    sole = hier[0][index][3]
    if cv2.contourArea(cnt) > 50:

        hull = cv2.convexHull(cnt)

        # img3 = img.copy()
        # black2 = black.copy()

        x,y,w,h = cv2.boundingRect(cnt)
        rect = (x,y,w,h)
        rects.append(cv2.boundingRect(cnt))

        # cv2.rectangle(img2,(x,y),(x+w,y+h),(0,255,0),2)

        # cv2.drawContours(img2, [hull],-1,(0,255,0),3)
        # g2 = cv2.cvtColor(black2 , cv2.COLOR_BGR2GRAY)
        # r , t2 = cv2.threshold(g2,127,255,cv2.THRESH_BINARY)
        # cv2.imshow("t2.jpg" , t2)
        #
        # masked = cv2.bitwise_and(img2,img2,mask = t2)
        # cv2.imshow("masked.jpg",masked)

        # print(len(hull))
    index+=1

# print rects
# rects = cv2.groupRectangles(rects,5,1)
# print rects
# print rects
index = 0
os.mkdir(name,0755)
for (x,y,w,h) in rects:
    print x
    cv2.rectangle(img2,(x,y),(x+w,y+h),(0,255,0),2)
    index+=1
    croped = orginal[y:y+h,x:x+w]
    # cv2.imshow(index.__str__(),croped)
    cv2.imwrite(name+'/'+index.__str__()+'.jpeg',croped)

# cv2.imshow("original.jpg with",img2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()