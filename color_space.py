import cv2

img = cv2.imread("Resources/lena.png")


img2 = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.imshow("image",img)
cv2.imshow("image2",img2)

cv2.waitKey(0)