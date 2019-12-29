import cv2
import numpy as np
from goprocam import GoProCamera
from goprocam import constants
import time

cascPath = "/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml"
# faceCascade = cv2.CascadeClassifier(cascPath)
# gpCam = GoProCamera.GoPro()
# gpCam.gpControlSet(constants.Stream.BIT_RATE, constants.Stream.BitRate.B2_4Mbps)
# gpCam.gpControlSet(constants.Stream.WINDOW_SIZE, constants.Stream.WindowSize.W480)
cap = cv2.VideoCapture("udp://127.0.0.1:10000")
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    cv2.imshow("GoPro OpenCV", frame)
    cv2.waitKey(1)

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
