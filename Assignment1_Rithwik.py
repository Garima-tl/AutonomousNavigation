import cv2
import numpy as np
import matplotlib.pyplot as plt

def detect_tennis_ball(image_path):

    image = cv2.imread(image_path)
    output = image.copy()

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_green = np.array([29, 86, 6])
    upper_green = np.array([64, 255, 255])

    
    mask = cv2.inRange(hsv, lower_green, upper_green)

    masked_image = cv2.bitwise_and(image, image, mask=mask)
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blurred = cv2.GaussianBlur(gray, (9, 9), 2)

    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=1.2, minDist=1,
                               param1=100, param2=30, minRadius=0, maxRadius=0)

    
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        if len(circles) > 0:  
            (x, y, r) = circles[0]  
            cv2.circle(output, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

    plt.figure(figsize=(10, 10))
    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.subplot(1, 2, 2)
    plt.title("Detected Tennis Ball")
    plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
    plt.show()


image_path = 'tennisball.jpg'  
detect_tennis_ball(image_path)
