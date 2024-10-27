from ultralytics import YOLO
import win32api
from mss import mss
import numpy as np
model = YOLO('yolov8n-pose.pt')
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
    if len(results) > 0 and results[0].keypoints is not None:
        keypoints = results[0].keypoints.xy.cpu().numpy()
        for keypoint in keypoints:
            if np.any(keypoint):
                win32api.SetCursorPos((left+round(keypoint[0][0]), top+round(keypoint[0][1])))
                break