# Aimbot Scripts Collection

## Overview
This repository contains a collection of aimbot scripts utilizing the YOLOv8 (You Only Look Once) object detection model. These scripts are designed to enhance user interaction with computer applications and games by automatically detecting targets and adjusting the mouse cursor accordingly. Each script targets specific detection tasks, such as identifying human figures or other objects in real-time screen captures.

## Features
- **Real-time Object Detection:** Each script employs the YOLOv8 model for fast and accurate detection of specified objects or keypoints.
- **Dynamic Cursor Control:** Automatically moves the mouse cursor to detected objects, enabling enhanced interaction.
- **Customizable Capture Area:** Users can define the screen capture dimensions and regions according to their preferences.
- **Supports Multiple Object Classes:** Some scripts can detect various object classes, including humans and animals.

## Requirements
To run the scripts, you need to install the following Python packages:
- `ultralytics`
- `numpy`
- `pywin32`
- `mss`
- `keyboard` (for exit control)

You can install the required modules using pip:
bash
pip install ultralytics numpy pywin32 mss keyboard


## Scripts
### 1. Human Detection and Cursor Control
This script captures a specific area of the screen and uses the YOLOv8 pose detection model to identify human keypoints, automatically moving the mouse cursor to the first detected keypoint.

- **Usage:** 
  - Adjust the screen capture dimensions if necessary.
  - Ensure the YOLOv8 pose model weights (`yolov8n-pose.pt`) are correctly placed in your project directory.
  - Run the script.

### 2. Object Detection and Cursor Positioning
This script captures a defined screen area and uses the YOLOv8 object detection model to detect human figures. It moves the mouse cursor to the center of the bounding box of the detected person with the highest confidence.

- **Usage:**
  - Adjust the screen capture dimensions if necessary.
  - Ensure the YOLOv8 model weights (`yolov8n.pt`) are correctly placed in your project directory.
  - Run the script.

## Controls
- **Press 'q'** to exit the program in all scripts.

## Dynamic Screen Size Adjustment
All scripts are designed to automatically fetch the screen dimensions, making them compatible with various display setups without manual configuration.

## Contribution
Contributions are welcome! If you have suggestions for improvements or additional features, feel free to submit a pull request or open an issue.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer
These scripts are intended for educational purposes only. Use them responsibly and in compliance with relevant laws and guidelines. Misuse of aimbots in competitive gaming or other applications may lead to bans or penalties.

### Key Sections Explained:
1. **Overview:** Provides a brief introduction to the repository and its purpose.
2. **Features:** Lists the key functionalities of the scripts.
3. **Requirements:** Specifies the necessary libraries and how to install them.
4. **Scripts:** Details about each specific script available in the repository, including how to use them.
5. **Controls:** Indicates how users can interact with the scripts, specifically the exit command.
6. **Dynamic Screen Size Adjustment:** Highlights the feature of automatic screen dimension detection.
7. **Contribution:** Encourages collaboration and contributions to the project.
8. **License:** Mentions the licensing terms.
9. **Disclaimer:** Warns users about the responsible use of the scripts.

