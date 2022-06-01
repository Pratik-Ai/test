import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("Resources/lena.png",cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(image,220,225,cv2.THRESH_BINARY)

kernal = np.ones((7,7),np.uint8)

dialation = cv2.dilate(mask,kernal,iterations=2)
erode = cv2.erode(mask,kernal,iterations=2)
opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal)
opening1 = cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernal)
opening2 = cv2.morphologyEx(mask,cv2.MORPH_ELLIPSE,kernal)
opening3 = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal)
opening4 = cv2.morphologyEx(mask,cv2.MORPH_HITMISS,kernal)
opening5 = cv2.morphologyEx(mask,cv2.MORPH_BLACKHAT,kernal)
opening6 = cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernal)
opening7 = cv2.morphologyEx(mask,cv2.MORPH_RECT,kernal)
opening8 = cv2.morphologyEx(mask,cv2.MORPH_CROSS,kernal)

titles = ['dialation','erode','opening','opening1','opening2','opening3','opening4','opening5','opening6','opening7','opening8']

image = [dialation, erode, opening, opening1, opening2, opening3,opening4,opening5,opening6,opening7,opening8]

for i in range(11):
    plt.subplot(4,4, i+1)
    plt.imshow(image[i],cmap="gray")
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()