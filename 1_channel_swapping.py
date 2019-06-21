import cv2

img = cv2.imread("imori.jpg")
r=img[:,:,2].copy()
g=img[:,:,1].copy()
b=img[:,:,0].copy()

img[:,:,0]=r
img[:,:,1]=g
img[:,:,2]=b

cv2.imwrite("1_channel_swapping.jpg",img)