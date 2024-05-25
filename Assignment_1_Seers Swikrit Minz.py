import numpy as np
import cv2 
 
img = cv2.imread('E:\PROG\ROBOTICS SUMMER PROJECT\ten.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img1 =  cv2.GaussianBlur(img, (3, 3), 0)
 
circles = cv2.HoughCircles(img1,cv2.HOUGH_GRADIENT,0.5,10,
 param1=45,param2=50,minRadius=80,maxRadius=150)
 
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
 # draw the circle
 cv2.circle(img1,(i[0],i[1]),i[2],(0,255,0),2)

 
cv2.imshow('detected circles',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()