from ultralytics import YOLO
import win32api
from mss import mss
import numpy as np

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 2560, 1600
WIDTH, HEIGHT = 1000, 800
LEFT = (SCREEN_WIDTH - WIDTH) // 2
TOP = (SCREEN_HEIGHT - HEIGHT) // 2
CONFIDENCE_THRESHOLD = 0.35

# Initialize YOLO model and screen capture
model = YOLO('yolov8n.pt')
sct = mss()
monitor = {"top": TOP, "left": LEFT, "width": WIDTH, "height": HEIGHT}

# Preallocate memory for the screenshot
screenshot = np.empty((HEIGHT, WIDTH, 3), dtype=np.uint8)

while True:
    # Update the screenshot
    screenshot[:] = np.array(sct.grab(monitor))[..., :3]
    results = model(screenshot, show=True)
    
    # Check if any objects are detected
    if len(results[0].boxes.xyxy) > 0:
        # Get the bounding box coordinates, class label and confidence score
        boxes, confs, classes = results[0].boxes.xyxy, results[0].boxes.conf, results[0].boxes.cls
        
        # Filter out 'person' class with high enough confidence
        persons = [(box, conf) for box, conf, cls in zip(boxes, confs, classes) if int(cls) == 0 and conf >= CONFIDENCE_THRESHOLD]
        
        if persons:
            # Get the bounding box with the highest confidence
            box, _ = max(persons, key=lambda x: x[1])
            
            # Calculate the center of the bounding box
            center_x = int(((box[0].item() + box[2].item()) / 2))
            center_y = int(((box[1].item() + box[3].item()) / 2))
            
            # Move the cursor to the center of the bounding box
            win32api.SetCursorPos((LEFT + center_x, TOP + center_y))
