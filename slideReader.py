#libraries
import cv2
import pytesseract
from PIL import Image


#my files
from FrameOps import *
from diffFrame import *
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

#init object
frameOps = FrameOps()

#video to survey
vid = cv2.VideoCapture('hd1.mp4')

#holds the frames before export
frameHolder = []


currentFrame, framesLeft = frameOps.getNextFrame(vid, 50)
frameHolder.append(currentFrame)
prevCrop = frameOps.cropFrame(currentFrame, "mid")
while framesLeft == True:
    
    currentFrameCrop = frameOps.cropFrame(currentFrame, "mid")
    if (currentFrameCrop.all() != prevCrop.any()):
        frameHolder.append(currentFrame)
    
    prevCrop = currentFrameCrop
    
    currentFrame, framesLeft = frameOps.getNextFrame(vid, 50)

print(len(frameHolder))
count = 0
for x in frameHolder:
    cv2.imwrite("imgDump\\slide" +str(count) +".jpeg", x)
    count = count+1

    
#img = cv2.imread("Capture2.png")

#text = pytesseract.image_to_string(img)
#print(text)

#cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("---done---")