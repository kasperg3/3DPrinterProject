import urllib

import cv2
import numpy as np
import requests
from goprocam import GoProCamera
from goprocam import constants


gpCam = GoProCamera.GoPro()
gpCam.mode(constants.Mode.PhotoMode, constants.Mode.SubMode.Photo.Single_H5)

url = gpCam.take_photo()
print(url)
resp = requests.get(url, stream=True).raw
image = np.asarray(bytearray(resp.read()), dtype="uint8")
image = cv2.imdecode(image, cv2.IMREAD_COLOR)

# for testing
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 600,600)
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()