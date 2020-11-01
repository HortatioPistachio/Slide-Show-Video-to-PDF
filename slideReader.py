#libraries
import cv2




#my files
import FrameOps
from diffFrame import *
from FrameDiffTests import *
import ImgTools

#video to survey
vid = cv2.VideoCapture('slideShort.mp4')


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

ImgTools.ConvertToPdf(r'imgDump/slide')
print("---done---")