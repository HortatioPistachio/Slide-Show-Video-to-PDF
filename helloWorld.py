import cv2

img = cv2.imread('bitcoin.jpeg',0)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("hello world")