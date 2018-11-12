import cv2
import numpy as np
from collections import deque
# from matplotlib import pyplot as plt
# import pytesseract as tes


def rotateMat(img):
    rows,cols = img.shape;
    M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
    dst = cv2.warpAffine(img,M,(cols,rows))
    return dst


img = cv2.imread('add.jpg')
# img = cv2.resize(img,(600,300))
# denoised = img;
denoised = cv2.medianBlur(img,7)
# denoised = cv2.GaussianBlur(img,(5,5),0)
# denoised = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)

# # text = tes.image_to_string(img,lang='sin')
# cv2.namedWindow("loaded",cv2.WINDOW_NORMAL)
# cv2.namedWindow("denoised",cv2.WINDOW_NORMAL)
# cv2.imshow("loaded",img)
# cv2.imshow("denoised",denoised)
# print (text)
print ("starting")
gray_img = cv2.cvtColor(denoised,cv2.COLOR_BGR2GRAY)
gaussianadaptivethresimg = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                                 cv2.THRESH_BINARY_INV, 11, 2)

# cv2.namedWindow("thresholded",cv2.WINDOW_NORMAL)
# cv2.imshow("thresholded",gaussianadaptivethresimg)
# gaussianadaptivethresimg = rotateMat(gaussianadaptivethresimg);
# plt.subplot(221), plt.hist(gaussianadaptivethresimg);
# plt.subplot(222),plt.imshow('noise removed',gray_img)
# plt.subplot()
# plt.show()
# rows, cols = gaussianadaptivethresimg.shape
# print(gaussianadaptivethresimg)
# print ("rows ", rows, " cols ", cols)

hist = cv2.reduce(gaussianadaptivethresimg,1,cv2.REDUCE_AVG).reshape(-1)
# thist = cv2.reduce(gaussianadaptivethresimg,0,cv2.REDUCE_AVG).reshape(-1)

# print("herer")
th=0
# print (hist)
H,W = img.shape[:2]

# uppers = [y for y in range (2,H-2) if(hist[y]<=hth) and hist[y-1]<=hth and hist[y-2]<=hth  and hist[y+1]>hth  and hist[y+2]>hth ]
# lowers = [y for y in range (2,H-2) if(hist[y]>lth) and hist[y-1]>lth and hist[y-2]>lth and hist[y+1]<=lth and hist[y+2]<=lth ]
uppers = [y for y in range (H-1) if(hist[y]<=th) and hist[y+1]>th ]
lowers = [y for y in range (H-1) if(hist[y]>th) and hist[y+1]<=th ]


for y in uppers:
    cv2.line(gray_img, ( 0, y ),(W ,y), (0,255,0) , 1)

for y in lowers:
    cv2.line(gray_img, ( 0 , y), (W, y),  (0,255,0) , 1)


rows = deque()
characters = deque()
# print (uppers)
# print (lowers)
for y in range(0,uppers.__len__()):
    row = gray_img[uppers[y]:lowers[y],0:W]
    rows.append(row)
    # print (row)
    # cv2.imshow(y.__str__(), row)

for y in range(0,rows.__len__()):
    row = rows.popleft()

    gaussianadaptivethresrowimg = cv2.adaptiveThreshold(row, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                                        cv2.THRESH_BINARY_INV, 11, 2)

    rhist = cv2.reduce(gaussianadaptivethresrowimg,0,cv2.REDUCE_AVG).reshape(-1)
    # cv2.imshow(y.__str__()+"tres",gaussianadaptivethresrowimg)
    RH,RW = row.shape[:2]
    # print(row.shape[:2])
    rth = 2
    lefts = [x for x in range (RW-1) if(rhist[x]<=rth) and rhist[x+1]>rth ]
    rights = [x for x in range (RW-1) if(rhist[x]>rth) and rhist[x+1]<=rth ]
    # print("hist")
    # print(rhist)
    # print ("-")
    # print(lefts)
    # print(rights)

    for x in lefts:
        cv2.line(row, ( x, 0 ),(x ,RH), (0,255,0) , 1)

    for x in rights:
        cv2.line(row, ( x, 0), (x, RH),  (0,255,0) , 1)
    # cv2.imshow(y.__str__(),row)


    for x in range(0,lefts.__len__()):
        rh,rw = row.shape[:2]
        # print(row.shape[:2])
        char = row[0:rh,lefts[x] :rights[x]]
        if(y==2):characters.append(char)
        # cv2.imshow(x.__str__()+"C",char)

chimg = characters.__getitem__(0)
cpchimg = np.array(chimg,copy=True)
# cv2.imshow("copy ",cpchimg)

ym,xm = cpchimg.shape

mask = np.ones(cpchimg.shape,cpchimg.dtype) * 255

for j in range(1,ym-1):
    start = -1;
    end = -1;
    for i in range(1,xm-1):
        if( start==-1):
            # print cpchimg[j]
            timg = cv2.adaptiveThreshold(cpchimg, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                         cv2.THRESH_BINARY_INV, 11, 2)
            # print timg[j,:]
            cv2.imshow("chad",timg)
            if( timg[j,i]==255 and timg[j,i+1]==0):
                start = i+1
                # print ("sum ",su)
        else:
            if ( timg [j,i] ==0 and timg[j,i+1]==255 ):
                end = i
                resp = timg[j,start:end]
                # print ("resp ",resp)
                su = np.sum(timg[2:j+1,i:i+1])
                cont = False
                if(j>0):
                    cont = np.isin(0,mask[j-1,start:end])
                if(su<=500 or cont):
                    print ("row : ",j," st : ",start," en : ",end)
                    mask[j,start:end] = np.zeros(resp.shape,resp.dtype)
                # print ("alt ",timg[j,start:end])
                start =-1
                end = -1
                # print ("row : ",j," st : ",start," en : ",end)


# ccvh,ccvw = cpchimg.shape[:2]
# st = ccvw/2
# for y in range(ccvh):
#     for x in range(0)


# cv2.namedWindow("final ",cv2.WINDOW_NORMAL)
# cv2.namedWindow("final",cv2.WINDOW_NORMAL)
cv2.imshow("final",gray_img)
cv2.imshow("cpchar",mask)
cv2.resizeWindow("final",600,300)
cv2.waitKey(0)
cv2.destroyAllWindows()




