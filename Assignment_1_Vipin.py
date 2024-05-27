import cv2
import numpy as np
import matplotlib.pyplot as plt


def detect_tennis_ball(image_path):
    # Step 1: Read the input image
    image = cv2.imread(image_path)
    # output = image.copy()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Step 2: Apply Gaussian Blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (9, 9), 2)

    # Step 3: Apply Canny Edge Detection
    # edges = cv2.Canny(blurred, 100, 150)

    # Step 4: Apply Hough Circle Transform
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=1.2, minDist=20,
                               param1=100, param2=50, minRadius=10, maxRadius=400)

    # Step 5: Draw detected circles
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            # Draw the outer circle
            cv2.circle(image, (x, y), r, (0, 255, 0), 4)
            # cv2.rectangle(output, )
            # Draw the center of the circle
            cv2.circle(image, (x, y), 2, (255, 0, 0), 3)

    # Display the result
    plt.figure(figsize=(10,10))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Detected Ball!!")
    plt.axis("off")
    plt.show()

# Example usage
detect_tennis_ball("tennis_ball.jpg")
