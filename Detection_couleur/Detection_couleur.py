###Code###
#Ce code met en oeuvre la methode de segmentation du snake
##########
import numpy as np
from matplotlib import pyplot as plt
import math
from cv2 import cv2
from PIL import Image


#récupération des bandes en noir
colorImage = cv2.imread("Images_Resistance/resistance_9.png")
grayImage = cv2.imread("Images_Resistance/resistance_9.png",0)
ret,tresh=cv2.threshold(grayImage,190,255,cv2.THRESH_BINARY_INV)
masked=cv2.bitwise_and(colorImage, colorImage,mask=tresh)

cv2.imshow('monImage',tresh)
cv2.waitKey(0)

cv2.imshow('monImage',masked)
cv2.waitKey(0)
cv2.imshow('monImage',colorImage)
cv2.waitKey(0)