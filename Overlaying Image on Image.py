"""
HOMOGRAPHY
Given that we have a few points in our train image and the location of same points in the query image we can find a relationship between  them. This can be done using feature detectors.This relationship is basically a matrix, and the process of finding it is know as Homography.

APPROACH:
1. We use feature detection to find some similar features between two images.
2. We find the homography matrix using these similarities.
3. Once we have the the matrix which relates the two images, we can find other points (such as the corner points) of the second image using the first image.
4. If we can find the corner points, then we can warp a new image/video according to this target image and overlay the new image/video on top of it.

Uses code from Feature Detection.py
"""
import numpy as np
import cv2

# webcam video is fixed at a warped angle of the input image i.e. imgTarget
webCam = cv2.VideoCapture(0)                                          # contains image on which we have to overlay
imgTarget = cv2.imread('C:/Users/Sakshee/Pictures/cards1.jpg')        # static image which is used for feature detection
video = cv2.VideoCapture('C:/Users/Sakshee/Videos/test_video.mp4')    # video to be overlayed

success, imgVideo = video.read()      # capturing the first frame of the video
# First we will be overlaying picture (first video frame) on picture (target image) and then move forward with overlaying an entire video

hT, wT, cT = imgTarget.shape
imgVideo = cv2.resize(imgVideo, (wT, hT))

orb = cv2.ORB_create(nfeatures=1000)
kp1, des1 = orb.detectAndCompute(imgTarget, None)

while True:
    success, imgWebcam = webCam.read()
    kp2, des2 = orb.detectAndCompute(imgWebcam, None)

    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)
    good = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good.append(m)

    print(len(good))

    imgFeatures = cv2.drawMatches(imgTarget, kp1, imgWebcam, kp2, good, None, flags=2)

    if len(good) > 20:
        srcPts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)      # source points
        dstPts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)      # destination points

        matrix, mask = cv2.findHomography(srcPts, dstPts, cv2.RANSAC, 5.0)
        # print(matrix)             # Transformation matrix

        # pts are the 4 corners of target image
        pts = np.float32([[0, 0], [0, hT], [wT, hT], [wT, 0]]).reshape(-1, 1, 2)
        # dst are the corners of the webcam image which are being predicted by pts of imgTarget using the homography
        # matrix obtained by feature detection
        dst = cv2.perspectiveTransform(pts, matrix)
        # img2 will draw a bounding box in the warped webcam image from the corner points predicted from imgTarget
        img2 = cv2.polylines(imgWebcam, [np.int32(dst)], True, (255, 0, 255), 2)

        # since we need to overlay a random image (the first frame of the video here), we need to warp it like the
        # Webcam image i.e. we make sure that the video frame is in the same perspective as webcam footage
        imgWarp = cv2.warpPerspective(imgVideo, matrix, (imgWebcam.shape[1], imgWebcam.shape[0]))

        cv2.imshow('Warp', imgWarp)
        cv2.imshow('Image 2', img2)
        cv2.imshow('Image Target', imgTarget)
        cv2.imshow('Video', imgVideo)
        cv2.imshow('Webcam', imgWebcam)
        cv2.imshow('Matching', imgFeatures)
        cv2.waitKey(0)                     # since delay is infinite, it will keep capturing only one frame in real time

    else:
        print('Could not find enough relevant matches therefore nothing to show')