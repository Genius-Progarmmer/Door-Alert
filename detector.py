import cv2
import os
import time
from datetime import datetime
import pygame
from ultralytics import YOLO


model = YOLO("yolov8n.pt")

pygame.mixer.init()
pygame.mixer.music.load("sounds/beep.wav")


camera = cv2.VideoCapture(0)


# create photo folder
if not os.path.exists("photos"):
    os.makedirs("photos")


person_was_here = False


def clean_photos():
    files = []

    for file in os.listdir("photos"):
        if file.endswith(".jpg"):
            path = "photos/" + file
            files.append((path, os.path.getctime(path)))

    # newest first
    files.sort(key=lambda x: x[1], reverse=True)

    # keep only 20
    for old in files[20:]:
        os.remove(old[0])


while True:

    success, frame = camera.read()

    if not success:
        break


    results = model(frame, verbose=False)

    person = False


    for result in results:
        for box in result.boxes:

            if model.names[int(box.cls[0])] == "person":
                person = True



    # New person appeared
    if person and not person_was_here:

        pygame.mixer.music.play()


        name = datetime.now().strftime(
            "photos/photo_%Y-%m-%d_%H-%M-%S.jpg"
        )


        cv2.imwrite(name, frame)


        # update latest photo
        cv2.imwrite("photos/latest.jpg", frame)


        clean_photos()


        print("Photo saved:", name)


    if not person:
        person_was_here = False
    else:
        person_was_here = True



    cv2.imshow("Security Camera", frame)


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break



camera.release()
cv2.destroyAllWindows()