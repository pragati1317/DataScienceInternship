# -*- coding: utf-8 -*-
"""PencilSketch.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11LtYfi-pJ3ObEyoyjm8ixWtVjU2Xx42D
"""

import numpy as np
import pandas as pd
import cv2

image=cv2.imread("Singer1.jpg")
## cv2.imshow() will not work
##cv2.waitKey(0)
tmp=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

_, alpha=cv2.threshold(tmp, 0, 255, cv2.THRESH_BINARY)
b,g,r=cv2.split(image)
rgba=[b,g,r,alpha]
dst=cv2.merge(rgba,4)
cv2.imwrite("image1.jpeg", dst)

image1=cv2.imread("image1.jpeg")
import matplotlib.pyplot as plt
plt.imshow(image1)
# plt.axis("off")
plt.show()

##Now converting the image in gray code
gray_image=cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image)
# plt.axis("off")
plt.show()

## Next step to invert the new grayscale image

inverted_image=255-gray_image
plt.imshow(inverted_image)
# ax=plt.axes()
# ax.set_facecolor("white")
# plt.axis("off")
plt.show()

## Now next step in the process is to blur the image by using the Gaussian function in OpenCv
blurred=cv2.GaussianBlur(inverted_image, (21, 21), 0)

inverted_blurred=255-blurred

pencil_sketch=cv2.divide(gray_image, inverted_blurred, scale=256.0)
plt.imshow(pencil_sketch)
# plt.axis("off")

plt.show()

