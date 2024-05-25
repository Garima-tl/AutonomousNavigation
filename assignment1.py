import cv2
import numpy as np
from google.colab.patches import cv2_imshow

image = cv2.imread('/content/image.png')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_green = np.array([29, 86, 6])
upper_green = np.array([64, 255, 255])

mask = cv2.inRange(hsv, lower_green, upper_green)



contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    area = cv2.contourArea(contour)
    
    if area > 1000:  
        (x, y), radius = cv2.minEnclosingCircle(contour)
        center = (int(x), int(y))
        radius = int(radius)
        
        cv2.circle(image, center, radius, (0, 0, 255), 4)

cv2_imshow(image)
