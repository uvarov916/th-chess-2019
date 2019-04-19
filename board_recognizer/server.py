import numpy as np
import cv2

cap = cv2.VideoCapture(1)

frame = cap.read()[1]
# res = cv2.resize(res, None, fx = 0.5, fy = 0.5, interpolation = cv2.INTER_CUBIC)
cv2.imwrite("image2.jpg", frame)

cap.release()
