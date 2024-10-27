from ultralytics import YOLO
import win32api
from mss import mss
import numpy as np

model = YOLO('yolov8n.pt')  # Use your YOLOv8 model
sct = mss()
screen_width, screen_height = 2560, 1600
width = 1300
height = 600
left = (screen_width - width) // 2
top = (screen_height - height) // 2
monitor = {"top": top, "left": left, "width": width, "height": height}

while True:
    screenshot = np.array(sct.grab(monitor))[..., :3]
    results = model(screenshot, show=True)
    if len(results[0].boxes.xyxy) > 0:  # Check if any objects are detected
        for result in results[0].boxes.xyxy:
            # Get the bounding box coordinates
            x1, y1, x2, y2 = result[:4]
            # Calculate the center of the bounding box
            center_x = int((x1 + x2) / 2)
            center_y = int((y1 + y2) / 2)
            # Move the cursor to the center of the bounding box
            win32api.SetCursorPos((left+center_x, top+center_y))
            break