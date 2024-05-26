import cv2
import numpy as np
import matplotlib.pyplot as plt

imgpath = str(input("enter the path of your canny edge detected image:"))

max=int(input("enter the maximum radius of circular things you want to detect:"))
min=int(input("enter the minimum radius of circular things you want to detect:"))

  
image = cv2.imread(imgpath)

if image is None:
    print("Error: Image not found.")
    exit()


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


blurred = cv2.GaussianBlur(gray, (9, 9), 2)


circles = cv2.HoughCircles(
    blurred, 
    cv2.HOUGH_GRADIENT, dp=1.2, minDist=30,
    param1=50, param2=30, minRadius=min, maxRadius=max
)

# Ensure some circles were found
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")

    # Draw the circles on the original image
    for (x, y, r) in circles:
        cv2.circle(image, (x, y), r, (0, 255, 0), 4)
        cv2.rectangle(image, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

    # Show the output image
    plt.figure(figsize=(10, 10))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Detected balls")
    plt.axis("off")
    plt.show()
else:
    print("No circles were found.")
    