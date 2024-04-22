import cv2
import numpy as np

img = cv2.imread('color_text.jpg')
print(img.shape)
new_img = np.zeros(img.shape, dtype='uint8')


# находим контуры изображения
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (9, 9), 0)
img = cv2.Canny(img, 10, 30)

con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
print(con)

cv2.drawContours(new_img, con[0:95], -1, (238, 0, 133), 2)
cv2.drawContours(new_img, con[94:224], -1, (0, 0, 255), 2)
cv2.drawContours(new_img, con[224:500], -1, (0, 255, 0), 2)


cv2.imshow('Result', new_img)


cv2.waitKey(0)