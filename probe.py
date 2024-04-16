import cv2
import numpy as np

photo = np.zeros((600, 600, 3), dtype='uint8')

# i=0
# k=0
# for _ in range(40):
#     photo[0+i:30+i, :] = (50+k, 255-k/7, 240)
#     i += 15
#     k += 5

# cv2.circle(photo, (photo.shape[1] // 2, photo.shape[0] // 2), 230, (255, 200, 230), thickness=2)

cv2.circle(photo, (photo.shape[1] // 2, photo.shape[0] // 2), 230, (255, 200, 230), thickness=3)

cv2.ellipse(photo, center=(photo.shape[1] // 2, 330), axes=(30, 30), angle=0, startAngle=0, endAngle=180, color=(0, 255, 0), thickness=3)
cv2.ellipse(photo, center=(photo.shape[1] // 2, 330), axes=(70, 70), angle=0, startAngle=0, endAngle=180, color=(0, 255, 0), thickness=3)

cv2.line(photo, (photo.shape[1] // 2 - 30, 330), (photo.shape[1] // 2 - 30, 250), (255, 0, 0), thickness=3)
cv2.line(photo, (photo.shape[1] // 2 - 70, 330), (photo.shape[1] // 2 - 70, 250), (255, 0, 0), thickness=3)
cv2.line(photo, (photo.shape[1] // 2 + 30, 330), (photo.shape[1] // 2 + 30, 250), (255, 0, 0), thickness=3)
cv2.line(photo, (photo.shape[1] // 2 + 70, 330), (photo.shape[1] // 2 + 70, 250), (255, 0, 0), thickness=3)

cv2.ellipse(photo, center=(photo.shape[1] // 2 - 50, 250), axes=(20, 20), angle=180, startAngle=0, endAngle=180, color=(0, 0, 255), thickness=3)
cv2.ellipse(photo, center=(photo.shape[1] // 2 + 50, 250), axes=(20, 20), angle=180, startAngle=0, endAngle=180, color=(0, 0, 255), thickness=3)


cv2.imshow('Photo', photo)
cv2.waitKey(0)
