# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 21:10:51 2020

@author: amanb
"""

import cv2

cap=cv2.VideoCapture(0); #using default camera of system
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('First Video',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
