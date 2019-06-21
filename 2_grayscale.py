import cv2
import numpy as np

# read

img = cv2.imread("imori.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imwrite("2_grayscale_1.jpg",gray)


b = img[:,:,0].copy()
g = img[:,:,1].copy()
r = img[:,:,2].copy()

out = 0.2126*r + 0.7152*g + 0.0722*b

out = out.astype(np.uint8)

cv2.imwrite("2_grayscale_2.jpg",out)