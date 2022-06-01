import cv2
img=cv2.imread("Resources/lena.png")
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,thresh=cv2.threshold(img_gray,127,255,0)
conto,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print("contours"+str(len(conto)))

contour_img=cv2.drawContours(img,conto,-1,(255,0,255),3)
cv2.imshow("imgg",contour_img)
cv2.waitKey(0)