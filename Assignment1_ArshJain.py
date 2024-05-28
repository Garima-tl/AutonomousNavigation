#code not working on VSCode
#GOOGLE COLAB LINK
"""https://colab.research.google.com/drive/1FY-F5Krpc11tG2WFL-3RQYrsdBbE495G?usp=sharing"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def detect_tennis_ball(image_path):
    image = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise and improve edge detection
    blurred = cv2.GaussianBlur(gray, (9, 9), 2)

    # Perform Canny edge detection
    edges = cv2.Canny(blurred, 50, 150)

    # Use Hough Circle Transform to detect circles
    circles = cv2.HoughCircles(
        edges,
        cv2.HOUGH_GRADIENT,
        dp=1.2,
        minDist=50,
        param1=100,
        param2=30,
        minRadius=10,
        maxRadius=50
    )

    # If some circles are detected, let's highlight them
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            # Draw the circle in the output image
            cv2.circle(image, (x, y), r, (0, 255, 0), 4)

    # Convert BGR image to RGB for displaying with matplotlib
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Display the resulting image using matplotlib
    plt.imshow(image_rgb)
    plt.axis('off')  # Hide axis
    plt.show()


image_path = 'ball3.jpg'
detect_tennis_ball(image_path)
