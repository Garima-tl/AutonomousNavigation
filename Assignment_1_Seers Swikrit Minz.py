from matplotlib import pyplot as plt
import numpy as np
import os
import cv2

#TAKING INPUT IMAGE
image = cv2.imread('INPUT_IMAGE')

#CONVERTING BGR TO RGB
re_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#CONVERTING RGB TO GRAYSCALE
gray = cv2.cvtColor(re_image, cv2.COLOR_RGB2GRAY)

#APPLYING GAUSSIAN FILTER
img1 =  cv2.GaussianBlur(gray, (3, 3), 1.8)

#APPLYING CANNY EDGE DETECTION
edges = cv2.Canny(img1, 50, 100)

#APPLYING HOUGH TRANSFROM FOR CIRCLES
circles = cv2.HoughCircles(edges,cv2.HOUGH_GRADIENT,1.2,60,
 param1=45,param2=60,minRadius=10,maxRadius=170)

#CONVERTING FLOATING POINT TO INT
circles = np.uint16(np.around(circles))

for i in circles[0,:]:
 #DRAWING CIRCLES
 cv2.circle(re_image,(i[0],i[1]),i[2],(255,0,0),2)

#IMAGE DISPLAY WITH IDENTIFIED CIRCLES
plt.imshow(re_image)
plt.show()
