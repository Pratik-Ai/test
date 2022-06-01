import cv2

img = cv2.VideoCapture("Resources/sample-5s.mp4")

while True:
    imv, src = img.read()
    cv2.imshow("imge",src)
    cv2.waitKey(1)

