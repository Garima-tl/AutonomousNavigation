import cv2
import numpy as np
def detect_tennis_ball(image):
    # Convert the image to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # Define the color range for detecting a tennis ball (in HSV)
    lower_yellow = np.array([29, 86, 6])
    upper_yellow = np.array([64, 255, 255])

    # Create a mask to isolate the yellow color
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # Apply Gaussian blur to the mask to reduce noise
    blurred = cv2.GaussianBlur(mask, (9, 9), 2)

    # Use Canny edge detection
    edges = cv2.Canny(blurred, 50, 150)

    # Use Hough Transform to detect circles
    circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=1.2, minDist=30,
                               param1=50, param2=30, minRadius=10, maxRadius=100)

    # If circles are detected, draw them
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            # Draw the outer circle
            cv2.circle(image, (x, y), r, (0, 255, 0), 4)
            # Draw the center of the circle
            cv2.circle(image, (x, y), 3, (0, 128, 255), 3)
    return image
# Load the image
image = cv2.imread('ball.jpg')
# Detect tennis ball
result_image = detect_tennis_ball(image)
# Display the result
cv2.imshow('Detected Tennis Ball', result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()