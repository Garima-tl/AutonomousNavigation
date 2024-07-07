# Autonomous Navigation of MARS Rover 

Project Objective
Our project aims to achieve precise object detection and localization using advanced computer vision techniques and stereo camera technology, exploring efficient ways of localization without GPS. Key contributions include:

Utilizing Hough transform and Canny edge detection for accurate ball detection.
Calculating the center of detected balls.
Integrating ZED stereo cameras with ROS (Robot Operating System) to obtain exact 3D coordinates of detected balls.
Implementing YOLOv for detecting objects such as cuboids.
Extracting centroids of detected cuboids and computing their 3D coordinates relative to the stereo camera setup.
This integration enables robust spatial understanding and localization capabilities crucial for applications in robotics, automation, and scenarios where GPS signals may be unreliable or unavailable.

# TASK 1 - You have to write an efficient code for detecting a tennis ball using Canny edge detection and Hough transform. The goal is to accurately identify the ball's circular shape while minimizing errors and optimizing performance. (You can use blurring , masking, parameter tunning etc for optimizing your code ).

1. Fork this GitHub repo.  
2. Clone your forked repo to your laptop locally.  
3. Copy your Python file into the repo directory; the file should be named `Assignment_1_yourname`.  
4. Stage and commit your Python file to your local repository.  
5. Push whatever you have done into your forked branch.  
6. Click "New pull request," add a title `rollno_assignment1_rover` and a brief message, then submit.
