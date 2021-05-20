# Image features are unique parts of an image that help defining it. In other words these are specific patterns
# or specific features which are unique, can be easily tracked and can be easily compared.
# (for example in a scenery, an image patch of the sky would be difficult to identify since its spread over a lot of area
# but to identify an image patch containing the top of pine cone tree is easier thus making it a better feature. )

import cv2
import numpy as np

img1 = cv2.imread('C:/Users/Sakshee/Pictures/query.jpg', 0)
img2 = cv2.imread('C:/Users/Sakshee/Pictures/train.jpg', 0)

# ORB detector: Oriented FAST and Rotated BRIEF
orb = cv2.ORB_create(nfeatures=1000)

# keypoint 1 and descripter 1
# the detector will find keypoints which are unique to the image and mark them
# descripters are an array or bin of numbers with a shape of (500, 32)- the orb detector by default tries to find 500 features
# and for each feature tries to describe it in 32 values
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)
print(kp1)             # type = list
print(len(kp1))        # since we have set nfeatures to 1000 it will find 1000 keypoints
print(des1.shape)      # each key point is described by 32 calues

imgKp1 = cv2.drawKeypoints(img1, kp1, None)
imgKp2 = cv2.drawKeypoints(img2, kp2, None)

# We try to match descriptors from 2 different images to see how much similarity we are getting. We use BFMatcher.knnMatch() to get k best matches
# Brute-Force matcher is simple. It takes the descriptor of one feature in first set and is matched with all other features in second
# set using some distance calcs
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)    # k as 2 so we will be returned with two features
print(matches)

#how do we decide which is a good match
good = []
for m, n in matches:                #since we set k as 2 there are 2 values that we can unpack
    if m.distance < 0.75*n.distance:
        good.append([m])

img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=2)

#img3 = cv2.resize(img3, (0,0), None, 0.3, 0.3)
print(good)
print(len(good))    # to know the number of good matches

cv2.imshow('Result', img3)
cv2.imshow('ImageKp1', imgKp1)
cv2.imshow('ImageKp2', imgKp2)
cv2.imshow('Image1', img1)
cv2.imshow('Image2', img2)
cv2.waitKey(0)
