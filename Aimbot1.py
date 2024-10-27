"""
Color-Based Screen Interaction Script
Based on OpenCV
This script captures a specified region of the screen, identifies contours based on a color range 
(in this case, orange), and performs a click action on the largest detected contour. The script
is designed to run in real-time, allowing for continuous screen tracking and interaction based 
on color detection.

Requirements:
    - Install necessary modules:
        pip install numpy opencv-python pyautogui mss

Controls:
    - Press 'q' to exit the program.
"""

import cv2
import numpy as np
import pyautogui
from mss import mss

# Prevents pyautogui from raising an exception when moving to the screen edges
pyautogui.FAILSAFE = False

# Define the lower and upper boundaries for the color (HSV color space)
# Adjust color range values to fit your specific target color
lower_color = np.array([5, 50, 50])   # Adjust for orange
upper_color = np.array([15, 255, 255])

# Get screen dimensions and define region for screenshot capture
screen_width, screen_height = pyautogui.size()
capture_width, capture_height = 1300, 600
left = (screen_width - capture_width) // 2
top = (screen_height - capture_height) // 2
monitor = {"top": top, "left": left, "width": capture_width, "height": capture_height}

# Initialize screen capture tool
sct = mss()

while True:
    # Capture and process the screenshot
    screenshot = np.array(sct.grab(monitor))
    frame = cv2.cvtColor(screenshot, cv2.COLOR_RGBA2RGB)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask based on defined color range and extract result
    mask = cv2.inRange(hsv_frame, lower_color, upper_color)
    color_detection = cv2.bitwise_and(frame, frame, mask=mask)

    # Find contours based on the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        # Locate the largest contour, calculate its center, and move the cursor there
        largest_contour = max(contours, key=cv2.contourArea)
        moments = cv2.moments(largest_contour)
        
        if moments["m00"] != 0:
            cX = int(moments["m10"] / moments["m00"])
            cY = int(moments["m01"] / moments["m00"])
            pyautogui.click(left + cX, top + cY)  # Click at the center of the contour
            # Optional: Uncomment the line below to move cursor without clicking
            # pyautogui.moveTo(left + cX, top + cY)

    # Display result for visual feedback
    cv2.imshow("Color Detection", color_detection)

    # Exit loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Clean up
cv2.destroyAllWindows()
