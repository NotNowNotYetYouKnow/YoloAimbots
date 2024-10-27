"""
Human Keypoint Detection and Cursor Control Script
This script captures a specified area of the screen and employs the YOLOv8 pose detection model 
to identify human keypoints. It automatically moves the mouse cursor to the position of the 
first detected keypoint, facilitating real-time interaction based on human pose detection.

Requirements:
    - Install necessary modules:
        pip install ultralytics numpy pywin32 mss

Controls:
    - Press 'q' to exit the program.
"""

from ultralytics import YOLO
import win32api
from mss import mss
import numpy as np

# Load the YOLOv8 pose model
model = YOLO('yolov8n-pose.pt')

# Initialize screen capture with mss
sct = mss()

# Get screen dimensions using win32api
screen_width = win32api.GetSystemMetrics(0)  # Width
screen_height = win32api.GetSystemMetrics(1)  # Height

# Define the region for screen capture
width, height = 1300, 600
left, top = (screen_width - width) // 2, (screen_height - height) // 2
monitor = {"top": top, "left": left, "width": width, "height": height}

# Main loop for real-time keypoint detection and cursor positioning
while True:
    screenshot = np.array(sct.grab(monitor))[..., :3]  # Capture screen region and drop alpha channel
    results = model(screenshot, show=True)  # Run YOLOv8 inference on the screenshot
    
    # Process detected keypoints
    if results and results[0].keypoints is not None:
        keypoints = results[0].keypoints.xy.cpu().numpy()
        for keypoint in keypoints:
            if np.any(keypoint):  # Check if keypoint is valid
                win32api.SetCursorPos((left + int(keypoint[0][0]), top + int(keypoint[0][1])))
                break  # Exit loop once cursor is set to the first detected keypoint
