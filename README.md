# DoorAlert

DoorAlert is a Python-based AI security project that uses YOLO to detect people through a camera. When a person is detected, the program triggers a beep alert.

The project demonstrates how computer vision and real-time object detection can be used to create a simple automated alert system.

## Features

* Real-time person detection
* YOLO-powered object detection
* Camera-based monitoring
* Automatic beep alert when a person is detected
* Python implementation
* Real-time video processing

## How It Works

DoorAlert continuously processes frames from a camera and uses a YOLO model to identify objects.

When the model detects a person, DoorAlert triggers a beep to notify the user.

```text
Camera
   |
   v
Video Frames
   |
   v
YOLO Object Detection
   |
   v
Person Detected?
   |
   +---- No ----> Continue Monitoring
   |
   +---- Yes ---> Beep Alert
```

## Built With

* Python
* Ultralytics YOLO
* OpenCV
* YOLOv8

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/DoorAlert.git
```

### 2. Navigate to the Project

```bash
cd DoorAlert
```

### 3. Install Dependencies

```bash
pip install ultralytics opencv-python
```

## Setup

Before running DoorAlert, add the alert sound.

Create a folder named:

```text
sounds
```

Inside the `sounds` folder, place the sound file:

```text
beep.wav
```

Your project should look like this:

```text
DoorAlert/
|
├── detector.py
├── yolov8n.pt
├── sounds/
│   └── beep.wav
├── requirements.txt
└── README.md
```

Make sure the sound file is named exactly:

```text
beep.wav
```

The program uses this sound when a person is detected.

## Running the Detector

After completing the setup, run the detector:

```bash
python detector.py
```

Make sure your camera is connected and available to the program.

When a person is detected, DoorAlert will trigger the `beep.wav` alert.

## YOLO Model

DoorAlert uses a YOLO model from Ultralytics for object detection.

The project uses:

```text
yolov8n.pt
```

The model processes camera frames and identifies people in real time.

## Project Structure

```text
DoorAlert/
|
├── detector.py
├── yolov8n.pt
├── sounds/
│   └── beep.wav
├── requirements.txt
└── README.md
```

## Example Behavior

When no person is detected:

```text
Monitoring...
```

When a person is detected:

```text
Person detected!
Beep alert triggered.
```

The `beep.wav` file will play as the alert.

## Purpose

DoorAlert was created as a practical project for learning and experimenting with:

* Artificial intelligence
* Computer vision
* Object detection
* YOLO
* OpenCV
* Real-time camera processing
* Python programming
* Automated alerts

## License

This project is open source and available under the MIT License.

## Author

Developed as a Python computer vision project using YOLO for real-time person detection and automated alerts.
