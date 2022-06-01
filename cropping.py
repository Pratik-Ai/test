import cv2

img = cv2.imread("Resources/lena.png")
print(img.shape)
cro = img[80:500,80:100]

cv2.imshow("image",img)
cv2.imshow("cropi",cro)
cv2.waitKey(0)