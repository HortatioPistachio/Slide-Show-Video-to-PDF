import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread("bitcoin.jpeg")

text = pytesseract.image_to_string(img)
print(text)

#cv2.imshow('image', img)

print("---done---")