import matplotlib.pyplot as plt 
import cv2 as cv 
import numpy as np 
import os 


def houghCircleTransform(): 
    root = os.getcwd()
    imgPath = os.path.join(root,'demoImages//tesla.jpg')
    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    imgGray = cv.medianBlur(imgGray,21)

    # dp - downsample steps 
    # minDist - min distance between detected circles 
    # param1 - higher threshold for canny edge
    # param2 - accumulator threshold (lower more circle,s higher less circles)
    circles = cv.HoughCircles(imgGray,cv.HOUGH_GRADIENT,dp=1,minDist=600,param1=200,param2=15,minRadius=100,maxRadius=150)
    circles = np.uint16(np.around(circles))

    for circle in circles[0,:]: 
        cv.circle(imgRGB,(circle[0],circle[1]),circle[2],(255,255,255),10)

    plt.figure() 
    plt.imshow(imgRGB)
    plt.show() 
    
if __name__ == '__main__': 
    houghCircleTransform() 
