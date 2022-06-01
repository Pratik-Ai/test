import cv2

img = cv2.imread("Resources/lambo.png")
height, width = img.shape[:2]
matrix = cv2.getRotationMatrix2D((height/2,width/2),45,1)
rotten = cv2.warpAffine(img,matrix,(height,width))
cv2.imshow("image",img)
cv2.imshow("rotten",rotten)
cv2.waitKey(0)