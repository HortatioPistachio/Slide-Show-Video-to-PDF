#libraries
import cv2
import pytesseract


#my files
from frameExtractor import *
from diffFrame import *
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

vid = cv2.VideoCapture('hd1.mp4')

frames = frameExtractor(vid)

img = cv2.imread("bitcoin.jpeg")

text = pytesseract.image_to_string(img)
print(text)

#cv2.imshow('image', img)

print("---done---")