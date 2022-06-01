import cv2

img = cv2.imread("Resources/lambo.png")

img1 = cv2.resize(img,(200,200),10)

cv2.imshow("image",img)
cv2.imshow("image1",img1)

cv2.waitKey(0)