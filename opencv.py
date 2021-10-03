# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 12:51:22 2021

@author: Neel
"""

import cv2
import random

num = random.randint(0, 1000)

videoCaptureObject = cv2.VideoCapture(0)
result = True
while(result):
    ret,frame = videoCaptureObject.read()
    cv2.imwrite("image" + str(num) + ".jpg",frame)
    result = False
videoCaptureObject.release()
cv2.destroyAllWindows()
