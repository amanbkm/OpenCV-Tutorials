# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 20:31:05 2020

@author: amanb
"""

import cv2
img=cv2.imread('lena.jpg',-1)
#print(img)
cv2.imshow('lena',img)
#Capture the keystroke in K and destroy if ESC is pressed and save a copy if s is pressed
k=cv2.waitKey(0)

if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite('lena_copy.png',img)