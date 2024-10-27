import cv2
import numpy as np
import pyautogui
from mss import mss
pyautogui.FAILSAFE=False

# Define the lower and upper boundaries for the color in the HSV color space
lower_red = np.array([5, 50, 50])# for orange
upper_red = np.array([15, 255, 255])

# lower_red = np.array([170, 100, 100]) #for red, it masks everything but red and we track that or whatever you wish to
# upper_red = np.array([180, 255, 255])

# Get screen size
screen_width, screen_height = pyautogui.size()

# Define the region of the screen to capture
width = 1300
height = 600
left = (screen_width - width) // 2
top = (screen_height - height) // 2
monitor = {"top": top, "left": left, "width": width, "height": height}

sct = mss()

while True:
    # Process screenshot
    screenshot = np.array(sct.grab(monitor))
    frame = cv2.cvtColor(screenshot, cv2.COLOR_RGBA2RGB)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Find largest contour and move cursor
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    largest_contour = max(contours, key=cv2.contourArea, default=None)
    if largest_contour is not None:
        moments = cv2.moments(largest_contour)
        cX = int(moments["m10"] / moments["m00"]) if moments["m00"] else 0
        cY = int(moments["m01"] / moments["m00"]) if moments["m00"] else 0
        pyautogui.click(left+cX, top+cY)
        # pyautogui.moveTo(left+cX, top+cY)

    # Display result and break loop if 'q' is pressed
    cv2.imshow("Red Detection", res)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
cv2.destroyAllWindows()