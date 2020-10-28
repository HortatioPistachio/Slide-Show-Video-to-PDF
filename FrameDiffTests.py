import FrameOps
import numpy as np
import cv2

class FrameDiffTest:
    
    def __init__(self, initFrame):
        self.pastFrame= initFrame
        self.pastBWSum = 0

    #this function returns an all black canvas
    def blank(self):
        return np.zeros(shape=[512,512,3], dtype = np.uint8)
        
    #this test, crops out the middle of the picture (gernerall the useful part)
    #and check whether or not it has changed since the last frame
    #doesnt work great becuase the video quality is so shotty it always changes
    #changed to b&W to reduce noise
    def frameMidChange(self,currentFrame):
        currentFrameCrop = cv2.cvtColor( FrameOps.cropFrame(currentFrame, 'mid'), cv2.COLOR_BGR2GRAY)
        prevCrop = cv2.cvtColor(FrameOps.cropFrame(self.pastFrame, 'mid'), cv2.COLOR_BGR2GRAY)
        self.pastFrame = currentFrame
        print( abs(np.sum(currentFrameCrop) - np.sum(prevCrop) ) )
        if ( abs( np.sum(currentFrameCrop) - np.sum(prevCrop) ) > 100000 ):
            return  currentFrame

        return self.blank()


    #this function converts to BW and then sum up all the pixels on the screen and then compare to the previous sum
    def sumTest(self, currentFrame):
        currentFrameBW = cv2.cvtColor( currentFrame, cv2.COLOR_BGR2GRAY)
        #prevFrameBW = cv2.cvtColor( self.pastFrame, cv2.COLOR_BGR2GRAY)

        self.pastFrame = currentFrame

        currentVal = np.sum(currentFrameBW) // 10000
        #preVal = np.sum(prevFrameBW) // 10000
        preVal = self.pastBWSum
        self.pastBWSum = currentVal
        #print( str(currentVal) + "    "+str(preVal) + "     " + str( abs(currentVal-preVal)) )

        #the constant value here is the tolerance to pick a slide to be save,  100 works well
        #too high you will miss slides, too low and you will get double ups
        if(abs(currentVal-preVal) > 100):
            return currentFrame
        return self.blank()
        