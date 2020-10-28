#libraries
import cv2
import pytesseract
from PIL import Image


#my files
import FrameOps
from diffFrame import *
from FrameDiffTests import *
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

#init object
#frameOps = FrameOps()

#video to survey
vid = cv2.VideoCapture('hd1.mp4')


currentFrame, framesLeft = FrameOps.getNextFrame(vid, 20)

prevCrop = FrameOps.cropFrame(currentFrame, "mid")

frameDiffTests = FrameDiffTest( currentFrame)
count = 0
while framesLeft == True:
    newFrame = frameDiffTests.sumTest(currentFrame)

    if(np.sum(newFrame) != 0):
        cv2.imwrite("imgDump/slide" +str(count) +".jpeg", newFrame)
        count = count+1
    
    currentFrame, framesLeft = FrameOps.getNextFrame(vid, 20)

#img = cv2.imread("Capture2.png")

#text = pytesseract.image_to_string(img)
#print(text)

#cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("---done---")