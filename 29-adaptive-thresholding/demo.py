import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 
import os 


def adaptiveThresholding(): 
    root = os.getcwd() 
    imgPath = os.path.join(root,'demoImages//tesla.jpg')
    imgGray = cv.imread(imgPath,cv.IMREAD_GRAYSCALE)

    plt.figure() 
    plt.subplot(141)
    plt.imshow(imgGray,cmap='gray') 
    plt.title('gray')

    plt.subplot(142)
    _, imgThres = cv.threshold(imgGray,70,255,cv.THRESH_BINARY)
    plt.imshow(imgThres,cmap='gray')
    plt.title('global thres')

    plt.subplot(143)
    maxValue = 255
    blockSize = 7 
    offsetC = 2 
    imgMean = cv.adaptiveThreshold(imgGray,maxValue,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,blockSize,offsetC)
    plt.imshow(imgMean,cmap='gray')
    plt.title('mean thres')

    plt.subplot(144)
    imgGaus = cv.adaptiveThreshold(imgGray,maxValue,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,blockSize,offsetC)
    plt.imshow(imgGaus,cmap='gray')
    plt.title('Gaus thres')


    plt.show() 

if __name__ == '__main__': 
    adaptiveThresholding() 

