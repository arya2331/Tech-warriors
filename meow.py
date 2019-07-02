import pytesseract
from PIL import Image
import cv2
img = cv2.imread('img.jpg',cv2.IMREAD_COLOR)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray=cv2.bilateralFilter(gray,11,17,17)
original=pytesseract.image_to_string(gray,config='')
print(original)
cv2.imshow('gray',gray)
cv2.waitKey(0)