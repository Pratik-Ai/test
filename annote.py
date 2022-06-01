import cv2

img = cv2.imread("Resources/lena.png")

cap = img.copy()

line = cv2.line(cap,(0,0),(200,200),(255,0,255),4)

cv2.imshow("img",img)
cv2.imshow("img1",cap)

cv2.waitKey(0)