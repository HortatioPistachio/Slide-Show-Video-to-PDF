#libraries
import cv2

#my files
import FrameOps
from FrameDiffTests import *
import ImgTools
from VideoReader import VideoReader

def main():

    #video to survey
    #vid = cv2.VideoCapture('slideShort.mp4')
    video = VideoReader("hd1.mp4",40)
    

    #currentFrame, framesLeft = FrameOps.getNextFrame(vid, 40)
    video.update()
    currentFrame = video.getFrame()
    remainingFrames = video.frameLeft()
    

    frameDiffTests = FrameDiffTest( currentFrame)
    count = 0
    while remainingFrames > 0:
        newFrame = frameDiffTests.sumTest(currentFrame)

        if(np.sum(newFrame) != 0):
            cv2.imwrite("imgDump/slide" +str(count) +".jpeg", newFrame)
            count = count+1
        
        currentFrame = video.getFrame()
        remainingFrames = video.frameLeft()

    ImgTools.ConvertToPdf(r'imgDump/slide')
    print("---done---")


main()