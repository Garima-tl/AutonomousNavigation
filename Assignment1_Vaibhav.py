import numpy as np
import cv2

image_path = r"C:\Users\vaibh\OneDrive\Pictures\balls.jpg"

image = cv2.imread(image_path, 0)
output = cv2.imread(image_path, 1)

blurred = cv2.GaussianBlur(image, (11, 11), 0)

circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, 30,
                           param1=60, param2=30, minRadius=0, maxRadius=0)

if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:
        cv2.circle(output, (x, y), r, (0, 255, 0), 3)
        cv2.rectangle(output, (x - 2, y - 2), (x + 2, y + 2), (0, 255, 0), -1)

cv2.imshow("Detections", output)
cv2.imwrite("CirclesDetection.jpg", output)
cv2.waitKey()
cv2.destroyAllWindows()
