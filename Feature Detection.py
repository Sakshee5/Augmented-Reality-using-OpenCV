"""
Image features are unique parts of an image that help defining it. In other words these are specific patterns or specific features which are  unique, can be easily tracked and can be easily compared.
For example in a scenery, an image patch of the sky would be difficult to identify since its spread over a lot of area
but to identify an image patch containing the top of pine cone tree is easier thus making it a better feature.
"""

import cv2
import numpy as np

img1 = cv2.imread('C:/Users/Sakshee/Pictures/query.jpg', 0)
img2 = cv2.imread('C:/Users/Sakshee/Pictures/train.jpg', 0)   # an image similar to img1 but at a different warped angle

# ORB detector: Oriented FAST and Rotated BRIEF
orb = cv2.ORB_create(nfeatures=1000)      # default value = 500

""" 
Keypoint 1(kp1) and descripter 1(des1)
The detector will find keypoints which are unique to the image and mark them descripters are an array or bin of numbers with a shape of (1000, 32) since we are using nfeatures = 1000
# and for each feature tries to describe it in 32 values 
"""

kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)
print(kp1)             # type = list
print(len(kp1))        # since we have set nfeatures to 1000 it will find 1000 keypoints
print(des1.shape)      # each key point is described by 32 calues

imgKp1 = cv2.drawKeypoints(img1, kp1, None)
imgKp2 = cv2.drawKeypoints(img2, kp2, None)

"""
No we will try to match the descriptors obtained from the two images to check how similar they are. We use BFMatcher.knnMatch() to get the k best matches.
Brute-Force matcher takes the descriptor of one feature from the first set and matches it with all other features in second set using some distance calculations
"""

bf = cv2.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)    # k as 2 so we will be returned with two features

# We use distance calculations to decide whether the 2 most similar features selected are a good match. We do this by using a ratio test on the two matches returned by the brute force matcher to check how similar they are to each other.
good = []
for m, n in matches:                #since we set k as 2 there are 2 values that we can unpack
    if m.distance < 0.75*n.distance:
        good.append([m])

img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=2)

print(good)
print(len(good))
# we get a number around 100 which tells us that from the 100 features detected, we found 100 good matches which relate the two images

cv2.imshow('Result', img3)      # final good matches visualized
cv2.imshow('ImageKp1', imgKp1)  # detected features marked on the first image
cv2.imshow('ImageKp2', imgKp2)  # detected features marked on the second image
cv2.imshow('Image1', img1)
cv2.imshow('Image2', img2)
cv2.waitKey(0)
