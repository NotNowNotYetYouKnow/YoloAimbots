"""
Human Detection and Cursor Control Script
This script captures a specified area of the screen and utilizes the YOLOv8 object detection model 
to identify human figures. It automatically moves the mouse cursor to the center of the bounding 
box of the detected person with the highest confidence, enabling dynamic interaction based on human presence.

Requirements:
    - Install necessary modules:
        pip install ultralytics numpy pywin32 mss

Controls:
    - Press 'q' to exit the program (implementation needed).
"""

from ultralytics import YOLO
import win32api
import win32con
from mss import mss
import numpy as np
import keyboard  # Requires installation: pip install keyboard

# Get screen dimensions dynamically
SCREEN_WIDTH = win32api.GetSystemMetrics(0)  # Width
SCREEN_HEIGHT = win32api.GetSystemMetrics(1)  # Height

# Define capture area dimensions (adjustable)
WIDTH, HEIGHT = 1000, 800
LEFT = (SCREEN_WIDTH - WIDTH) // 2
TOP = (SCREEN_HEIGHT - HEIGHT) // 2
CONFIDENCE_THRESHOLD = 0.35  # Minimum confidence for detection

# Initialize the YOLO model and screen capture
model = YOLO('yolov8n.pt')  # Ensure the model path is correct
sct = mss()
monitor = {"top": TOP, "left": LEFT, "width": WIDTH, "height": HEIGHT}

# Preallocate memory for the screenshot
screenshot = np.empty((HEIGHT, WIDTH, 3), dtype=np.uint8)

while True:
    # Update the screenshot
    screenshot[:] = np.array(sct.grab(monitor))[..., :3]
    
    # Run YOLOv8 inference on the screenshot
    results = model(screenshot, show=True)
    
    # Check if any objects are detected
    if len(results[0].boxes.xyxy) > 0:
        # Extract bounding box coordinates, confidence scores, and class labels
        boxes, confs, classes = results[0].boxes.xyxy, results[0].boxes.conf, results[0].boxes.cls
        
        # Filter for detected 'person' class with confidence above the threshold
        persons = [(box, conf) for box, conf, cls in zip(boxes, confs, classes) if int(cls) == 0 and conf >= CONFIDENCE_THRESHOLD]
        
        if persons:
            # Get the bounding box with the highest confidence
            box, _ = max(persons, key=lambda x: x[1])
            
            # Calculate the center of the bounding box
            center_x = int((box[0].item() + box[2].item()) / 2)
            center_y = int((box[1].item() + box[3].item()) / 2)
            
            # Move the cursor to the center of the bounding box
            win32api.SetCursorPos((LEFT + center_x, TOP + center_y))
    
    # Exit condition (press 'q' to quit)
    if keyboard.is_pressed('q'):
        print("Exiting...")
        break
