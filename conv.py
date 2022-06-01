import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('Resources/lena.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
kernel = np.ones((15, 15), np.float32)/225
dst = cv2.filter2D(img, -1, kernel)
blur = cv2.blur(img, (15,15))
gblur = cv2.GaussianBlur(img, (15, 15), 0)
medblur = cv2.medianBlur(img, 5)
bilateral = cv2.bilateralFilter(img, 11, 75, 75)
titles = ['image', '2D Convolution', 'blur', 'gblur', 'medblur', 'bilateral']
images = [img, dst, blur, gblur, medblur, bilateral]
for i in range(6):
    plt.subplot(3, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
