# reading an image
import cv2

img = cv2.imread("Resources/lena.png")
imgi = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("image",img)
cv2.imshow("image1",imgi)
cv2.waitKey(0)
