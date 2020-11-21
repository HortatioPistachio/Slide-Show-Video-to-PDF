#libraries
import cv2

#my files
import FrameOps
from FrameDiffTests import *
import ImgTools
from VideoReader import VideoReader

def main():

    #video to survey
    #fileName = input("Enter filename: ")
    #video = VideoReader(fileName,40).start()
    video = VideoReader("seminarPreso.mp4",20).start()


    #currentFrame, framesLeft = FrameOps.getNextFrame(vid, 40)
    
    currentFrame = video.getFrame()
    remainingFrames = video.frameLeft()
    

    frameDiffTests = FrameDiffTest( currentFrame )
    count = 0
    
    while remainingFrames == True:

        if(frameDiffTests.test(currentFrame)):
            cv2.imwrite("imgDump/slide" +str(count) +".jpeg", currentFrame)
            count = count+1
        
        currentFrame = video.getFrame()
        remainingFrames = video.frameLeft()

    ImgTools.ConvertToPdf(r'imgDump/slide')
    print("---done---")


main()