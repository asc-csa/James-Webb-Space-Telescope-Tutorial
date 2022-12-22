# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 10:38:16 2022

@author: karora
"""

from imutils import contours
from skimage import measure
import numpy as np
import imutils
import cv2

image = cv2.imread(r'C:\Users\karora\Desktop\James_Webb_CADC\test4.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (11, 11), 0)

# create a threshold in  the image to reveal light regions

thresh = cv2.threshold(blurred, 100, 1000, cv2.THRESH_BINARY)[1]

# perform a connected component analysis on the thresholded
# image, then initialize a mask to store only the "large"
# components
labels = measure.label(thresh,  background=0)
mask = np.zeros(thresh.shape, dtype="uint8")

# loop over the unique components
for label in np.unique(labels):
    
	# ignore the background label
	if label == 0:
		continue
    
	# otherwise, construct the label mask and count the
	# number of pixels 
	labelMask = np.zeros(thresh.shape, dtype="uint8")
	labelMask[labels == label] = 255
	numPixels = cv2.countNonZero(labelMask)
    
	# if the number of pixels in the component is sufficiently
	# large, then add it to our mask of "large blobs"
	if numPixels > 20:
		mask = cv2.add(mask, labelMask)
        
# find the contours in the mask, then sort them from left to
# right
cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = contours.sort_contours(cnts)[0]

# loop over the contours
counter = 0 
for (i, c) in enumerate(cnts):
    counter = counter + 1
	# draw the bright spot on the image
	#(x, y, w, h) = cv2.boundingRect(c)
	#((cX, cY), radius) = cv2.minEnclosingCircle(c)
	#cv2.circle(image, (int(cX), int(cY)), int(radius),
		#(0, 0, 255), 3)
	#cv2.putText(image, "#{}".format(i + 1), (x, y - 15),
		#cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
        
# show the output image
#cv2.imshow("Image", image)
#cv2.waitKey()        
print(counter)
