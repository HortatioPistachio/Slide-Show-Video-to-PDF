#libraries
import cv2

#my files
import FrameOps
from FrameDiffTests import *
import ImgTools
from VideoReader import VideoReader

def main():

    #video to survey

    video = VideoReader("hd1.mp4",40).start()
    #video = VideoReader("slideShort.mp4",40).start()
    

    #currentFrame, framesLeft = FrameOps.getNextFrame(vid, 40)
    
    currentFrame = video.getFrame()
    remainingFrames = video.frameLeft()
    

    frameDiffTests = FrameDiffTest( currentFrame)
    count = 0
    while remainingFrames == True:
        newFrame = frameDiffTests.sumTest(currentFrame)

        if(np.sum(newFrame) != 0):
            cv2.imwrite("imgDump/slide" +str(count) +".jpeg", newFrame)
            count = count+1
        
        currentFrame = video.getFrame()
        remainingFrames = video.frameLeft()

    ImgTools.ConvertToPdf(r'imgDump/slide')
    print("---done---")


main()