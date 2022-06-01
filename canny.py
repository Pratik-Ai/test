import matplotlib.pyplot as plt
import numpy as np
import cv2
img = cv2.imread("Resources/lena.png")
edges = cv2.Canny(image=img, threshold1=100, threshold2=200)

cv2.imshow("image",img)
cv2.imshow("edge",edges)
cv2.waitKey(0)