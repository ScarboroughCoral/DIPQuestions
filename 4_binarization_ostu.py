import cv2
import numpy as np

img = cv2.imread("imori.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
H, W, C = img.shape
th=128
max_v=0

w=H*W

#calculate the threshold by using the ostu algorithm
for i in range(1,255):
    c0=gray[gray<i]
    c1=gray[gray>=i]
    w0=len(c0)/w
    w1=len(c1)/w
    m0=np.mean(c0) if len(c0)>0 else 0
    m1=np.mean(c1) if len(c1)>0 else 0
    v=w0*w1*((m0-m1)**2)
    if max_v<v:
        max_v=v
        th=i


print(th)



#binarize the img

gray[gray>=th]=255
gray[gray<th]=0

cv2.imwrite("4_ostu_binarization.jpg",gray);