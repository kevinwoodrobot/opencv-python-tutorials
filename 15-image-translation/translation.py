import os 
import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt 

def translation():
    root = os.getcwd()
    imgPath = os.path.join(root,'demoImages\\cutepic1.jpg')
    img = cv.imread(imgPath)
    
    T = np.array([[1,0,200],
                  [0,1,200]],dtype=np.float32)
    height,width,_ = img.shape
    '''
        cv.warpAffine(img,T,dim) - transforms image
            @param img Ndarray 
            @param T 2x3 np.array 
            @param dim Tuple output dimension
            @returns mxnx3 transformed image 
    '''
    imgTrans = cv.warpAffine(img,T,(width,height))
    cv.imshow('imgTrans',imgTrans)
    cv.waitKey(0)


    debug = 1 

if __name__ == '__main__': 
    translation() 
