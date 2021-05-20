"""
Uses code from Feature Detection.py and Overlaying Image on Image.py
"""
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
imgTarget = cv2.imread('C:/Users/Sakshee/Pictures/cards1.jpg')
myVid = cv2.VideoCapture('C:/Users/Sakshee/Videos/test_video.mp4')

# Boolean to tell us whether we have the target in our image or not
detection = False
# keep a count of frames we have displayed from our video
frameCounter = 0

success, imgVideo = myVid.read()
hT, wT, cT = imgTarget.shape
imgVideo = cv2.resize(imgVideo, (wT, hT))

orb = cv2.ORB_create(nfeatures=1000)
kp1, des1 = orb.detectAndCompute(imgTarget, None)

def stackImages(imgArray, scale, labels=[]):
    """
    Function to stack images togther in the form of an array so that only one output window contains all the results
    ARGUMENTS:
    imgArray - example [[img1, img2, ...imgn],[img1, img2, ...imgn], ...]
    scale - to scale the output window
    labels - label for each image to be displayed in the same format as imgArray
    RETURNS: stacked image
    """
    sizeW = imgArray[0][0].shape[1]
    sizeH = imgArray[0][0].shape[0]
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                imgArray[x][y] = cv2.resize(imgArray[x][y], (sizeW, sizeH), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((sizeH, sizeW, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
            hor_con[x] = np.concatenate(imgArray[x])
        ver = np.vstack(hor)
        ver_con = np.concatenate(hor)
    else:
        for x in range(0, rows):
            imgArray[x] = cv2.resize(imgArray[x], (sizeW, sizeH), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        hor_con = np.concatenate(imgArray)
        ver = hor
    if len(labels) != 0:
        eachImgWidth = int(ver.shape[1] / cols)
        eachImgHeight = int(ver.shape[0] / rows)
        print(eachImgHeight)
        for d in range(0, rows):
            for c in range(0, cols):
                cv2.rectangle(ver, (c * eachImgWidth, eachImgHeight * d),
                              (c * eachImgWidth + len(labels[d]) * 13 + 27, 30 + eachImgHeight * d), (255, 255, 255),
                              cv2.FILLED)
                cv2.putText(ver, labels[d], (eachImgWidth * c + 10, eachImgHeight * d + 20), cv2.FONT_HERSHEY_COMPLEX,
                            0.7, (255, 0, 255), 2)
    return ver


while True:

    success, imgWebcam = cap.read()
    imgAug = imgWebcam.copy()
    kp2, des2 = orb.detectAndCompute(imgWebcam, None)

    if detection == False:
        # sets the video back to frame zero
        myVid.set(cv2.CAP_PROP_POS_FRAMES, 0)
        frameCounter = 0

    else:
        # checks whether the video has reached it maximum number of frames. If yes, then it resets it so that the video can play again
        if frameCounter == myVid.get(cv2.CAP_PROP_FRAME_COUNT):
            myVid.set(cv2.CAP_PROP_POS_FRAMES, 0)
            frameCounter = 0

        success, imgVideo = myVid.read()
        imgVideo = cv2.resize(imgVideo, (wT, hT))

    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)
    good = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good.append(m)
    print(len(good))
    imgFeatures = cv2.drawMatches(imgTarget, kp1, imgWebcam, kp2, good, None, flags=2)

    if len(good) > 20:
        detection = True
        srcPts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
        dstPts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
        matrix, mask = cv2.findHomography(srcPts, dstPts, cv2.RANSAC, 5)
        print(matrix)

        pts = np.float32([[0, 0], [0, hT], [wT, hT], [wT, 0]]).reshape(-1, 1, 2)
        dst = cv2.perspectiveTransform(pts, matrix)
        img2 = cv2.polylines(imgWebcam, [np.int32(dst)], True, (255, 0, 255), 3)

        imgWarp = cv2.warpPerspective(imgVideo, matrix, (imgWebcam.shape[1], imgWebcam.shape[0]))

        # entire webcam image as black
        maskNew = np.zeros((imgWebcam.shape[0], imgWebcam.shape[1]), np.uint8)
        # fill the space where the image has been found to white
        cv2.fillPoly(maskNew, [np.int32(dst)], (255, 255, 255))
        # we inverse our mask because we'll be overlaying images using bitwise_and and bitwise_or next
        # we need to make sure which region (image or background) is white and which is black to overlay it accordingly
        maskInv = cv2.bitwise_not(maskNew)

        # as declared earlier we have imgAug as the webcam copy. By the command we are filling up all the white region with the actual 
        # background
        imgAug = cv2.bitwise_and(imgAug, imgAug, mask=maskInv)
        imgAug = cv2.bitwise_or(imgWarp, imgAug)

        imgStacked = stackImages(([imgWebcam, imgTarget, imgVideo, imgFeatures], [imgAug, imgWarp, maskNew, maskInv]), 0.5)
        imgStacked = cv2.resize(imgStacked, (1000, 600))

        cv2.imshow('imgStacked', imgStacked)
        cv2.waitKey(1)

        # iterating the frame counter so that it can check when it reaches the end and replays
        frameCounter += 1

    else:
        print('Could not find enough relevant matches therefore imgStacked not defined')