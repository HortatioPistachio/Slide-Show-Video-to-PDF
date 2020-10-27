#libraries
import cv2
import pytesseract


#my files
from frameExtractor import *
from diffFrame import *
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

#init object
frameOps = FrameOps()

vid = cv2.VideoCapture('slideShort.mp4')


currentFrame, framesLeft = frameOps.getNextFrame(vid, 20)

while framesLeft == True:
    #check for text in frame
    
    txt = pytesseract.image_to_string(currentFrame)
    print(txt)
    print("--end text--")
    currentFrame, framesLeft = frameOps.getNextFrame(vid, 20)


img = cv2.imread("Capture.png")

text = pytesseract.image_to_string(img)
print(text)

#cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("---done---")