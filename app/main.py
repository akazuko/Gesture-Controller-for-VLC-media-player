"""main module for the app"""
import cv2
import keyboard
import numpy as np

from face_detector import FaceDetector

def run():
    """app's entrypoint"""
    detector = FaceDetector()

    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        faces = detector.detect(image=gray)
        if any([x.get('confidence') > 0.95 for x in faces]):
            keyboard.press('space')

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run()
