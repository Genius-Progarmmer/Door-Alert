# DoorAlert

DoorAlert is a Python-based security project that uses computer vision and YOLO object detection to detect people through a camera and provide an alert when a person is detected.

## Description

DoorAlert is designed to demonstrate how real-time object detection can be used for a simple security system.

The program uses a camera as its input and processes the camera feed to detect people using a YOLO model.

## Technologies

- Python
- OpenCV
- Ultralytics YOLO
- YOLOv8
- Computer Vision

## Features

- Real-time camera detection
- Person detection using YOLO
- Visual detection results
- Security alert functionality
- Real-time video processing

## Challenges

One of the main challenges of this project was working with real-time camera input and integrating a YOLO object detection model.

Another challenge was processing camera frames continuously while keeping the detection system responsive.

## What I Learned

Through this project, I learned how to:

- Use YOLO for object detection
- Work with OpenCV camera input
- Process video frames in real time
- Integrate computer vision models into Python projects
- Build a basic security detection system

## Status

Completed

## Future Improvements

- Add more types of detected objects
- Improve detection accuracy
- Add sound notifications
- Add image or video recording when a person is detected
- Add a more advanced alert system

## Project Preview

DoorAlert provides a real-time camera view with YOLO-based person detection and an alert system when a person is detected.

## Installation

Clone the repository:

```bash
git clone https://github.com/Genius-Progarmmer/DoorAlert.git
````

Move into the project directory:

```bash
cd DoorAlert
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## How to Run

Run the main Python file:

```bash
python main.py
```

Make sure your camera is connected and available before starting the program.

## Project Structure

```text
DoorAlert/
├── main.py
├── yolov8n.pt
├── requirements.txt
└── README.md
```

## Author

**Genius-Progarmmer**

GitHub: https://github.com/Genius-Progarmmer
