import cv2
import numpy as np
import matplotlib.pyplot as plt
# Reading of the image
image_path = 'path_of_image.jpg'
img = cv2.imread(image_path, cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#gray scaling
gray_blurred = cv2.GaussianBlur(gray, (9, 9), 2) #gaussian blur
edges = cv2.Canny(gray_blurred, 50, 150)
circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=1.2, minDist=30,
                           param1=50, param2=30, minRadius=15,
maxRadius=50)

if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:
        cv2.circle(img, (x, y), r, (0, 255, 0), 4)
        cv2.rectangle(img, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.title('Tennis Ball')
plt.axis('on')
plt.show()
