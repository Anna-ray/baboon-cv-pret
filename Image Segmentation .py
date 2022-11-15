#!/usr/bin/env python
# coding: utf-8

#  # Segmentation with Contours Detection

# ## Canny Filter:

# In[5]:


import cv2
path= r'C:\Users\Root\Desktop\baboon.jpg'
img = cv2.imread(path,0)
edges = cv2.Canny(img, 100, 200)
#Canny filter
cv2.imshow("Edge", edges)
cv2.waitKey(0)


# ## Laplacien Filter

# In[6]:


import numpy as np
img = cv2.imread(path,0)
edge = cv2.Laplacian (img, cv2.CV_64F, ksize=3)
edge = np.uint8(np.absolute(edge))
cv2.imshow('Laplacian filter', edge)
cv2.waitKey()


# # Segmentation with region formation

# ## Global Threshold:

# In[10]:


img = cv2.imread(path,0)
ret,thresh1 = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,100,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,100,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,100,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,100,255,cv2.THRESH_TOZERO_INV)
titles = ['Image originale','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6) :
 cv2.imshow(titles[i], images[i])
cv2.waitKey()


# ## Otsu Method

# In[12]:


from matplotlib import pyplot as plt
img = cv2.imread(path,0)
# Seuillage manuel
ret1,th1 = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
# Seuillage par la méthode d'Otsu
ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_OTSU)
# euillage par la méthode d'Otsu après un filrage gaussien
blur = cv2.GaussianBlur(img,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_OTSU)
# plot all the images and their histograms
images = [img, 0, th1, img, 0, th2, blur, 0, th3]
titles = ['Image originale','Histogramme','Seuillage global (Seuil=100)','Image originale','Histogramme','Seuillage global(Otsu)','Image filtrée','Histogramme','Seuillage global (Otsu)']
for i in range(3):
 plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
 plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
 plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
 plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
 plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
 plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
plt.show()

