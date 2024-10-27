"""
YOLO Object Detection and Cursor Control Script
This script utilizes the YOLOv8 object detection model to continuously capture a specified
region of the screen, detect objects in real-time, and move the mouse cursor to the center 
of the first detected object. It is designed to run continuously, allowing for dynamic 
screen interaction based on object detection.

Requirements:
    - Install necessary modules:
        pip install ultralytics numpy pywin32 mss keyboard

Controls:
    - Press 'q' to exit the program.
"""

from ultralytics import YOLO
import win32api
import win32con
from mss import mss
import numpy as np
import time
import keyboard  # Requires installation: pip install keyboard

# Load the YOLO model
model = YOLO('yolov8n.pt')  # Ensure the model path is correct

# Initialize screen capture
sct = mss()
screen_info = win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)
screen_width, screen_height = screen_info
width, height = 1300, 600
left = (screen_width - width) // 2
top = (screen_height - height) // 2
monitor = {"top": top, "left": left, "width": width, "height": height}

print(f"Screen size: {screen_width}x{screen_height}")

# Main loop for object detection and cursor control
try:
    while True:
        # Capture the screen
        screenshot = np.array(sct.grab(monitor))[..., :3]
        
        # Perform object detection
        results = model(screenshot)

        # Check for detected objects
        if len(results[0].boxes.xyxy) > 0:  
            # Move cursor to the first detected object's center
            for result in results[0].boxes.xyxy:
                x1, y1, x2, y2 = result[:4]
                center_x = int((x1 + x2) / 2)
                center_y = int((y1 + y2) / 2)
                win32api.SetCursorPos((left + center_x, top + center_y))
                break  # Only move for the first detected object

        # Delay to reduce CPU usage
        time.sleep(0.1)

        # Exit condition
        if keyboard.is_pressed('q'):  # Press 'q' to exit
            print("Exiting...")
            break

except Exception as e:
    print(f"An error occurred: {e}")
