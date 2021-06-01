###Code###
#Ce code met en oeuvre la methode de segmentation du snake
##########
import numpy as np
from matplotlib import pyplot as plt
import math
import cv2
from PIL.Image import * 

Chemin="Images_Resistance/resistance_9.png"
#récupération des bandes en noir
colorImage = cv2.imread(Chemin)
grayImage = cv2.imread(Chemin,0)
ret,tresh=cv2.threshold(grayImage,193,255,cv2.THRESH_BINARY_INV)
masked=cv2.bitwise_and(colorImage, colorImage,mask=tresh)

ker1=cv2.getStructuringElement(cv2.MORPH_RECT,(18,11))
ouverture1=cv2.morphologyEx(masked, cv2.MORPH_OPEN, ker1) # ouverture de I par S

ker2=cv2.getStructuringElement(cv2.MORPH_RECT,(10,10))
ouverture2=cv2.morphologyEx(ouverture1, cv2.MORPH_OPEN, ker2) # ouverture de I par S


plt.axis('off')
plt.imshow(cv2.cvtColor(ouverture2, cv2.COLOR_BGR2RGB))
plt.show()
Recup_Couleur=open(Chemin)

premiere_bande=Image.getpixel(Recup_Couleur,(40,70))
print(premiere_bande)
deuxieme_bande=Image.getpixel(Recup_Couleur,(40,90))
print(deuxieme_bande)
troiseme_bande=Image.getpixel(Recup_Couleur,(40,120))
print(troiseme_bande)



