import cv2
import numpy as np
img = cv2.imread('image.jpg')
dim=(300,300)
resized = cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
cv2.imshow('Pic',resized)

img_not = cv2.bitwise_not(resized)
cv2.imshow('Invert',img_not)
cv2.imwrite('black.jpg',img_not)
cv2.destroyAllWindows()

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
print(pytesseract.image_to_string(Image.open('black.jpg')))

