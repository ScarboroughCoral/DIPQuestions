import cv2
import numpy as np
import math

img = cv2.imread("7.jpg")

# original image height & width
img_h = img.shape[0]
img_w = img.shape[1]

# polar coordinates maximum radius

max_radius = 1000

r_h_ratio = max_radius/img_h

new_h = 2*max_radius
new_w = 2*max_radius

new_img = 255*np.ones((new_h,new_w,3),dtype="u1")

# back reflection

for y in range(new_h):
    for x in range(new_w):

        r = math.sqrt((x-max_radius)**2+(y-max_radius)**2)
        if r>max_radius:
            continue
        theta = 0
        if x==max_radius:
            if y>=max_radius:
                theta = math.pi/2
            else:
                theta = -math.pi/2
        else:
            theta = math.atan2((y-max_radius),(x-max_radius))

        j = img_w*theta/(2*math.pi)
        i = img_h-(r/max_radius)*img_h-1

        if j<=0:
            j=-j
        else:
            j=img_w-j-1

        i,j=int(i),int(j)

        new_img[y,x,:]=img[i,j,:]

cv2.imwrite("7-2.jpg",new_img)

# fore reflection

# for i in range(img_w):
#     theta = 2*math.pi*(i/img_w)
#     for j in range(img_h):
#         r = ((img_h-j)/img_h)*max_radius-1
#         x = r*math.cos(theta)+max_radius
#         y = r*math.sin(theta)+max_radius
#         x,y = int(x),int(y)
#         new_img[y,x,:] = img[j,i,:]


# cv2.imwrite("result.jpg",new_img)