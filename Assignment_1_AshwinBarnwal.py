import cv2
import numpy as np

img = cv2.imread(input())

imgnew = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgnew = cv2.GaussianBlur(imgnew, (15, 15), 0)

circles = cv2.HoughCircles(imgnew, cv2.HOUGH_GRADIENT, dp=1.2, minDist=50,
                           param1=100, param2=30, minRadius=10, maxRadius=50)

if circles is not None:
    circles = np.uint8(np.around(circles))
    for i in circles[0, :]:
        cv2.circle(img, (i[0],i[1]), i[2], (0, 0, 255), 2)

cv2.imshow('new', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
