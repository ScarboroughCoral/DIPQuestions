import cv2

img = cv2.imread("imori.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

th = 128

gray[gray>=th]=255
gray[gray<th]=0

cv2.imwrite("4_binarization.jpg",gray)